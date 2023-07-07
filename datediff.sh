#!/bin/bash
read datesvar
dates_array=($datesvar)
result=$(( ($(date -d "${dates_array[1]} UTC" +%s) - $(date -d "${dates_array[0]} UTC" +%s)) / (60*60*24) ))
echo $result
