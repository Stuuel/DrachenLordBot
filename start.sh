#!/bin/bash

python3 lard.py &
while true
do
     git pull origin master > log.txt
     sleep 60s
     if ! grep -q 'Already up-to-date.' log.txt; then
          pkill -f lard.py
          sleep 10s
          python3 lard.py &
     fi     
     sleep 5m 
done
