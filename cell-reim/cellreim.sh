#!/bin/bash
# CD before running Python script so it's running in it's own directory
# when run from cron. Based on http://askubuntu.com/a/24527
cd /home/pi/CellReim
/home/pi/CellReim/cellreim.py
