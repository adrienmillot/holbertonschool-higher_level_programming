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

  print () {
    for (let row = 0; row < this.height; row++) {
      for (let column = 0; column < this.width; column++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }

  rotate () {
    const width = this.width;
    this.width = this.height;
    this.height = width;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
