#!/usr/bin/node
const fs = require('fs');

if (process.argv.length > 4) {
  const contentA = fs.readFileSync(process.argv[2], { encoding: 'utf-8' });
  const contentB = fs.readFileSync(process.argv[3], { encoding: 'utf-8' });
  fs.writeFile(process.argv[4], contentA + contentB, function (prmErrorMsg) {
    if (prmErrorMsg) {
      return console.log(prmErrorMsg);
    }
  });
} else {
  console.log('Usage: ./102-concat.js <filePathToSourceFile1> <filePathToSourceFile2> <filePathToDestinationFile>');
}
