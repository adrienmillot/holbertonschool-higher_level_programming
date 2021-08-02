#!/usr/bin/node

/**
 * prints a square
 */

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let row = 0; row < process.argv[2]; row++) {
    for (let column = 0; column < process.argv[2]; column++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
}
