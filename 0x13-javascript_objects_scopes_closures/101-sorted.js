#!/usr/bin/node

const occurrenceByUser = require('./101-data.js').dict;

const userByOccurrence = {};

for (const userId in occurrenceByUser) {
  const occurrence = occurrenceByUser[userId];
  if (!userByOccurrence[occurrence]) {
    userByOccurrence[occurrence] = [];
  }
  userByOccurrence[occurrence].push(userId);
}

console.log(userByOccurrence);
