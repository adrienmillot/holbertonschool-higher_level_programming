#!/usr/bin/node

/**
 * Rectangle class
 */
module.exports = class Rectangle {
  constructor (prmWidth, prmHeight) {
    if (prmWidth > 0 && prmHeight > 0) {
      this.width = prmWidth;
      this.height = prmHeight;
    }
  }
};
