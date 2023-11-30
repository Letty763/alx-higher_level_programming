#!/bin/bash
#Script to send request to given url and display response
curl -s "$1" | wc -c
