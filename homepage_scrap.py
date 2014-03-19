#!/usr/bin/python

################################################################################
# Scrapping of homepage GreenBook.org
#
# @author       Martin Kersner
# @email        m.kersner@gmail.com
# @date         19/03/2014
# @last_update  19/03/2014
################################################################################

from bs4 import BeautifulSoup
import requests
import csv

## downloading main page
response = requests.get("http://www.greenbook.org/")
html = response.text

s = BeautifulSoup(html)

## BROWSE BY MARKET RESEARCH SPECIALTIES #######################################
## Market Research Specialities

## BROWSE BY LOCATION ##########################################################
## MRS Market Reaserch Firms
## countries, states, metro area
writer_ctry = open('MRS_CTRY.csv','w')
writer_state = open('MRS_STATE.csv','w')
writer_metro = open('MRS_METRO.csv','w')

for link in s.find(id="browse_loc_MRS_CTRY").find_all("a"):
  writer_ctry.write(link.get("href") + "\t" + link.string + "\n")

for link in s.find(id="browse_loc_MRS_STATE").find_all("a"):
  writer_state.write(link.get("href") + "\t" + link.string + "\n")

for link in s.find(id="browse_loc_MRS_METRO").find_all("a"):
  writer_metro.write(link.get("href") + "\t" + link.string + "\n")

writer_ctry.close;
writer_state.close;
writer_metro.close;

## FCG Focus Group Facilities
## countries, states, metro area
writer_fcg_ctry = open('FCG_CTRY.csv','w')
writer_fcg_state = open('FCG_STATE.csv','w')
writer_fcg_metro = open('FCG_METRO.csv','w')

for link in s.find(id="browse_loc_FCG_CTRY").find_all("a"):
  writer_fcg_ctry.write(link.get("href") + "\t" + link.string + "\n")

for link in s.find(id="browse_loc_FCG_STATE").find_all("a"):
  writer_fcg_state.write(link.get("href") + "\t" + link.string + "\n")

for link in s.find(id="browse_loc_FCG_METRO").find_all("a"):
  writer_fcg_metro.write(link.get("href") + "\t" + link.string + "\n")

writer_fcg_ctry.close;
writer_fcg_state.close;
writer_fcg_metro.close;
