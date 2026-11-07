#!/usr/bin/env node
// Check that deploy.js serves all 36 emailed sample paths.
// Usage: node scripts/check-samples.mjs
import fs from 'fs';
import os from 'os';
import path from 'path';
import { pathToFileURL } from 'url';

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const deploy = fs.readFileSync(path.join(root, 'deploy.js'), 'utf8');
const start = deploy.indexOf('const W=');
if (start < 0) {
  console.error('deploy.js has no worker string');
  process.exit(1);
}
let i = start + 'const W='.length;
if (deploy[i] !== '"') {
  console.error('worker string is not a JSON string');
  process.exit(1);
}
let worker = '';
for (let j = i + 1; j < deploy.length; j++) {
  const c = deploy[j];
  if (c === '\\') {
    const n = deploy[j + 1];
    if (n === 'u') {
      worker += String.fromCharCode(parseInt(deploy.slice(j + 2, j + 6), 16));
      j += 5;
      continue;
    }
    const map = { '"': '"', '\\': '\\', n: '\n', r: '\r', t: '\t', '/': '/' };
    worker += map[n] ?? n;
    j += 1;
    continue;
  }
  if (c === '"') break;
  worker += c;
}

const file = path.join(os.tmpdir(), 'bwn-worker-check.mjs');
fs.writeFileSync(file, worker);
const mod = await import(pathToFileURL(file).href);
const paths = fs.readFileSync(path.join(root, 'samples', 'sent-paths.txt'), 'utf8')
  .split('\n').map((s) => s.trim()).filter(Boolean);
if (paths.length !== 36) {
  console.error('expected 36 sent paths, found ' + paths.length);
  process.exit(1);
}

let failed = 0;
function fail(msg) {
  console.error('FAIL', msg);
  failed += 1;
}

for (const p of paths) {
  const res = await mod.default.fetch(new Request('https://bizwinnow.com' + p));
  const body = await res.text();
  if (res.status !== 200) {
    fail(res.status + ' ' + p);
    continue;
  }
  const gov = p.startsWith('/govcon/');
  const title = gov ? 'Sample compliance matrix' : 'Free photo edit preview';
  if (!body.includes(title) || !body.includes('Business Win Now')) {
    fail('unexpected body ' + p);
    continue;
  }
  const slug = p.slice(p.lastIndexOf('/') + 1);
  const asset = gov ? p + '.png' : p + '.jpg';
  if (gov && !body.includes('/govcon/samples/' + slug + '.png') && !body.includes('<table')) {
    fail('govcon page has neither a matrix image nor a table ' + p);
    continue;
  }
  if (!gov) {
    const img = await mod.default.fetch(new Request('https://bizwinnow.com' + asset));
    const bytes = new Uint8Array(await img.arrayBuffer());
    if (img.status !== 200 || bytes[0] !== 0xff || bytes[1] !== 0xd8) {
      fail('listing jpeg ' + asset + ' status ' + img.status);
      continue;
    }
  }
  if (gov && body.includes('/govcon/samples/' + slug + '.png')) {
    const img = await mod.default.fetch(new Request('https://bizwinnow.com' + asset));
    const bytes = new Uint8Array(await img.arrayBuffer());
    const png = bytes[0] === 0x89 && bytes[1] === 0x50 && bytes[2] === 0x4e && bytes[3] === 0x47;
    if (img.status !== 200 || !png) {
      fail('matrix png ' + asset + ' status ' + img.status);
      continue;
    }
  }
  console.log('OK', res.status, body.length, p);
}

const shop = await mod.default.fetch(new Request('https://bizwinnow.com/shopify'));
const shopBody = await shop.text();
if (shop.status !== 200 || !shopBody.includes('$300') || !shopBody.includes('$1,000')) {
  fail('shopify price changed');
}
const re = await mod.default.fetch(new Request('https://bizwinnow.com/real_estate'));
const reBody = await re.text();
if (re.status !== 200 || !reBody.includes('/assets/re-room-3d-zoom.mp4') || !reBody.includes('re-room-still.jpg')) {
  fail('real-estate video section changed');
}
const video = await mod.default.fetch(new Request('https://bizwinnow.com/assets/re-room-3d-zoom.mp4'));
const vbytes = new Uint8Array(await video.arrayBuffer());
if (video.status !== 200 || vbytes.length < 1000) fail('3D zoom video missing');
const home = await mod.default.fetch(new Request('https://bizwinnow.com/'));
if (home.status !== 200) fail('home ' + home.status);

if (failed) {
  console.error(failed + ' check(s) failed');
  process.exit(1);
}
console.log('all 36 emailed sample paths are in this bundle');
