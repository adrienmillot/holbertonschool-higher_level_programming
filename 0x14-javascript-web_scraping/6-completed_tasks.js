#!/usr/bin/node
const request = require('request');

const users = {};

if (process.argv.length === 3) {
  request(process.argv[2], { json: true }, (err, res, body) => {
    if (err) { return console.error(err); }
    body.forEach(task => {
      if (task.completed === true) {
        if (task.userId in users) {
          users[task.userId] += 1;
        } else {
          users[task.userId] = 1;
        }
      }
    });
    console.log(users);
  });
}
