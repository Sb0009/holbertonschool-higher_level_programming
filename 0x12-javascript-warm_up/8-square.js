#!/usr/bin/node

const number = parseInt(process.argv[2]);

if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    let sequence = '';
    for (let j = 0; j < number; j++) {
      sequence += 'X';
    }
    console.log(sequence);
  }
}
