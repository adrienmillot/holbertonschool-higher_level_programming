#!/usr/bin/node

exports.converter = function (prmBase) {
  return function (prmNumber) {
    return prmNumber.toString(prmBase);
  };
};
