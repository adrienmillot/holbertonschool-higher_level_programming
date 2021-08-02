#!/usr/bin/node

/**
 * prints the first argument passed to it
 */

if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length > 2) {
  console.log(process.argv[2]);
}
