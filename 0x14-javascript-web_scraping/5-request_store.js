#!/usr/bin/node
const fs = require('fs');
const request = require('request');

if (process.argv.length === 4) {
  request(process.argv[2], (err, res, body) => {
    if (err) { return console.error(err); }

    fs.writeFile(process.argv[3], body, err => {
      if (err) { return console.error(err); }
    });
  });
}
