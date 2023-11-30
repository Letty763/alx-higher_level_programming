#!/bin/bash
# Sends a JSON file via  POST request to a  URL.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
