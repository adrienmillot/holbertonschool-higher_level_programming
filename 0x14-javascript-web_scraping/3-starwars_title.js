#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';

if (process.argv.length === 3) {
  request(url + process.argv[2], { json: true }, (err, res, body) => {
    if (err) { return console.log(err); }
    console.log(body.title);
  });
}
