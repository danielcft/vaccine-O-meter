#!/bin/python3
# Takes *ratio* as input, (ex: 0.20) and updates sense_hat LED display.
# curl https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/Denmark.csv | awk -F ',' 'END{print $8/5834700}' | xargs ./ratio_to_display.py

import sys
from sense_hat import SenseHat

ratio = float(sys.argv[1])
good = abs(round(ratio*64))

COLOR_BAD = [255,0,0] # red
COLOR_GOOD = [0,0,255] # blue

matrix = []
for x in range(0,8):
    for y in range(0,8):
        good -= 1
        if(good >= 0):
            matrix.append(COLOR_GOOD)
        else:
            matrix.append(COLOR_BAD)

# send matrix to pi
sense = SenseHat()
sense.set_pixels(matrix)
