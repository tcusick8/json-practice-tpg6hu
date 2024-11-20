#!/bin/bash

curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85" -o aviation.json

if jq empty aviation.json 2>/dev/null; then
  jq -r '.[].receiptTime' aviation.json | head -n 6
else
  echo "Invalid JSON or empty file. Please check aviation.json for details."
  exit 1
fi


