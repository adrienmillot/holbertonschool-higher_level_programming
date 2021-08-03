#!/usr/bin/node

/**
 * Return the number of occurences in a list
 * @param {*} prmList list to search in
 * @param {*} prmSearchElement element to compare
 */
exports.nbOccurences = function (prmList, prmSearchElement) {
  let count = 0;

  prmList.forEach(function (element) {
    if (element === prmSearchElement) {
      count++;
    }
  });

  return (count);
};
