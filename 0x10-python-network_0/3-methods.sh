#!/bin/bash
# Shows all HTTp headrs a server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
