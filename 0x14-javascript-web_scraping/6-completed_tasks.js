#!/usr/bin/node
const axios = require('axios');
axios.get(process.argv[2])
  .then(res => {
    const mydict = {};
    for (let i = 0; i < res.data.length; i++) {
      if (res.data[i].completed === true) {
        if (mydict[res.data[i].userId] === undefined) {
          mydict[res.data[i].userId] = 0;
        }
        mydict[res.data[i].userId] += 1;
      }
    } console.log(mydict);
  })
  .catch(err => {
    console.log(err);
  });
