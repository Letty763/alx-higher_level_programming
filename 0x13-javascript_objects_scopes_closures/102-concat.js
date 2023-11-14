u#!/usr/bin/node

const fs = require('fs');
const fileData1 = fs.readFileSync(process.argv[2], 'utf-8');
const fileData2 = fs.readFileSync(process.argv[3], 'utf-8');
fs.writeFileSync(process.argv[4], fileData1 + fileData2);
