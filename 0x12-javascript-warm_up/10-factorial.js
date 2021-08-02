#!/usr/bin/node

/**
 * Computes factorial of a number
 *
 * @param {*} a number
 *
 *  @returns factorial
 */
function factorial (a) {
  if (isNaN(a) || a === 0) {
    return (1);
  }

  return (factorial(a - 1) * a);
}

/**
 * computes and prints a factorial
 */

console.log(factorial(parseInt(process.argv[2])));
