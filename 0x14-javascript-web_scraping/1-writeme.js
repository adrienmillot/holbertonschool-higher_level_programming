#!/usr/bin/node
const fs = require('fs');

if (process.argv.length === 4) {
  fs.writeFile(process.argv[2], process.argv[3], err => {
    if (err) {
      return console.error(err);
    }
  });
}
