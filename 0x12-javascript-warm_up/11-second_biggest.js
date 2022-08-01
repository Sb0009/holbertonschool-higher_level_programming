#!/usr/bin/node
if (process.argv[3]) {
  process.argv.shift();
  process.argv.shift();
  const numbers = process.argv.map(function (x) {
    return parseInt(x);
  });
  const index = numbers.indexOf(Math.max(...numbers));
  numbers.splice(index, 1);
  console.log(Math.max(...numbers));
} else {
  console.log('0');
}
