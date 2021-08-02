#!/usr/bin/node
exports.callMeMoby = function (prmNb, prmFunction) {
  for (let i = 0; i < prmNb; i++) {
    prmFunction();
  }
};
