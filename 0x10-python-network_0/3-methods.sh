#!/bin/bash
# this sidplys all the http  url can take
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
