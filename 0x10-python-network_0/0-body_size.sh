#!/bin/bash
# this wll display the length of theurl
curl -s "$1" | wc -c 
