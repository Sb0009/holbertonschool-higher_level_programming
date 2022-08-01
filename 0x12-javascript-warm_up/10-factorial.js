#!/usr/bin/node
if (process.argv[2]) {
  const number = parseInt(process.argv[2], 10);
  console.log(factorial(number));
} else {
  console.log('1');
}

function factorial (number) {
  if (number === 1) {
    return (1);
  }
  return number * factorial(number - 1);
}
