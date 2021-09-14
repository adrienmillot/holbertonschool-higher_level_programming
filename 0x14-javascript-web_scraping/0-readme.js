#!/usr/bin/node
const fs = require('fs');

try {
  const data = fs.readFileSync(process.argv[2], 'utf-8');
  console.log(data);
} catch (err) {
  console.error(err);
}
