#!/usr/bin/node

exports.esrever = function (prmList) {
  const output = [];

  while (prmList.length) {
    output.push(prmList.pop());
  }

  return output;
};
