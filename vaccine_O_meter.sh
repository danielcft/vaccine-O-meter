#!/bin/bash

SOURCE_URL=https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/Denmark.csv

curl --silent $SOURCE_URL | awk -F ',' 'END{print $7/5834700}' | xargs ./display_ratio.py
