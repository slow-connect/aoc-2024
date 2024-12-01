#! /bin/bash

# This script is to get todays input, that `aoc.py` will
# parse to some better format

DAY=$1

if [[ -z $2 ]]; then
    YEAR=2023
else
    YEAR=$2
fi



FILE_URL="https://adventofcode.com/{$YEAR}/day/{$DAY}/input"
COOKIE=$(cat var/cookie)

FILE="var/$YEAR-$DAY.txt"

if [[ -f "$FILE" ]]; then
    cat $FILE
else
  curl -s -X GET $FILE_URL -H "Cookie: session=$COOKIE" > $FILE
  cat $FILE
fi
#
