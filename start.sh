#!/bin/bash

{
. /home/pi/PI/venv/bin/activate
until python /home/pi/PI/src/main.py; do
        echo "Server 'contemplant' crashed with exit code $?. Respawning... " >$
        sleep 1
done
} 1>/home/pi/PI/logs/log.out 2>&1