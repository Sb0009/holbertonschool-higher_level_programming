#!/usr/bin/node
const axios = require('axios');
const fs = require('fs');
axios.get(process.argv[2])
  .then(res => {
    fs.writeFile(process.argv[3], res.data, (err) => {
      if (err) throw err;
    });
  })
  .catch(err => {
    console.log(err);
  });
