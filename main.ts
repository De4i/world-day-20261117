/**
 * The World Day — make.fun entry for news-image-20261117.
 *
 * The front page beside this file is the entry: a 1024x1024 picture of
 * Tuesday 17 November 2026's world news, drawn from the day's reporting by
 * poster/poster.html. This program does one thing — it publishes those
 * exact bytes into the grader's output directory — so that the two graded
 * runs write the same file, byte for byte.
 *
 * Node 22, standard library only: nothing is installed before it runs, no
 * network is touched, and nothing outside this directory is read.
 *
 *   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
 */

import { copyFileSync, mkdirSync, openSync, readSync, closeSync, statSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
const POSTER = join(HERE, 'entry.png');
const OUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

/** The gate takes a whole image of at most one mebibyte. */
const LIMIT_BYTES = 1024 * 1024;

/** Every PNG opens with these eight bytes; a JPEG would open with FFD8FF. */
const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);

/** Read only the leading bytes: enough to identify the format, no big buffer. */
function head(path, length) {
  const fd = openSync(path, 'r');
  try {
    const buffer = Buffer.alloc(length);
    const read = readSync(fd, buffer, 0, length, 0);
    return buffer.subarray(0, read);
  } finally {
    closeSync(fd);
  }
}

function publish() {
  const size = statSync(POSTER).size;

  if (size > LIMIT_BYTES) {
    throw new Error(`${POSTER} is ${size} bytes, past the ${LIMIT_BYTES}-byte gate`);
  }
  const signature = head(POSTER, PNG_MAGIC.length);
  if (!signature.equals(PNG_MAGIC)) {
    throw new Error(`${POSTER} does not start with the PNG signature`);
  }

  mkdirSync(OUT_DIR, { recursive: true });
  const target = join(OUT_DIR, 'entry.png');
  copyFileSync(POSTER, target);

  // The graded runs are compared byte for byte, so confirm the copy landed
  // whole rather than reporting success on the strength of the write call.
  const written = statSync(target).size;
  if (written !== size) {
    throw new Error(`copied ${written} bytes, expected ${size}`);
  }
  process.stdout.write(`published entry.png, ${written} bytes, to ${target}\n`);
}

publish();
