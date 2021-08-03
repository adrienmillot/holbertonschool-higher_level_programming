#!/usr/bin/node

let argumentPrintedNb = 0;

exports.logMe = function (prmItem) {
  console.log(argumentPrintedNb + ': ' + prmItem);
  argumentPrintedNb++;
};
