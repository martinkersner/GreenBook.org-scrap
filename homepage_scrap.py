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
from parse import *

# SETTINGS
sep = "\t"

## downloading main page
response = requests.get("http://www.greenbook.org/")
html = response.text

bs = BeautifulSoup(html)

## BROWSE BY MARKET RESEARCH SPECIALTIES #######################################
## MARKET RESEARCH SPECIALTIES
head_mrsid = ["url", "category", "subcategory"]

## Buisness Issues
wr_mrsid1 = open('MRSID_1.csv', 'w')
parse_mrsid(bs, "MRSID_1", wr_mrsid1, head_mrsid, sep)
wr_mrsid1.close

## Research Solutions
wr_mrsid2 = open('MRSID_2.csv', 'w')
parse_mrsid(bs, "MRSID_2", wr_mrsid2, head_mrsid, sep)
wr_mrsid2.close

## Research Services
wr_mrsid3 = open('MRSID_3.csv', 'w')
parse_mrsid(bs, "MRSID_3", wr_mrsid3, head_mrsid, sep)
wr_mrsid3.close

## Industries & Demographics
wr_mrsid4 = open('MRSID_4.csv', 'w')
parse_mrsid(bs, "MRSID_4", wr_mrsid4, head_mrsid, sep)
wr_mrsid4.close

## Related Services & Software
wr_mrsid5 = open('MRSID_5.csv', 'w')
parse_mrsid(bs, "MRSID_5", wr_mrsid5, head_mrsid, sep)
wr_mrsid5.close

## International Expertise
wr_mrsid6 = open('MRSID_6.csv', 'w')
parse_mrsid(bs, "MRSID_6", wr_mrsid6, head_mrsid, sep)
wr_mrsid6.close

## BROWSE BY LOCATION ##########################################################
### MRS ALL MARKET RESEARCH FIRMS

## Countries
head_ctry = ["url", "country"]
wr_ctry = open('MRS_CTRY.csv', 'w')
parse_loc(bs, "browse_loc_MRS_CTRY", wr_ctry, head_ctry, sep)
wr_ctry.close

## States
head_state = ["url", "state"]
wr_state = open('MRS_STATE.csv', 'w')
parse_loc(bs, "browse_loc_MRS_STATE", wr_state, head_state, sep)
wr_state.close

## Metro area
head_metro = ["url", "metro_area"]
wr_metro = open('MRS_METRO.csv', 'w')
parse_loc(bs, "browse_loc_MRS_METRO", wr_metro, head_metro, sep)
wr_metro.close

### FCG FOCUS GROUP FACILITIES

## Countries, States, Metro area
head_ctry = ["url", "country"]
wr_fcg_ctry = open('FCG_CTRY.csv','w')
parse_loc(bs, "browse_loc_FCG_CTRY", wr_fcg_ctry, head_ctry, sep)
wr_fcg_ctry.close

## State
head_state = ["url", "state"]
wr_fcg_state = open('FCG_STATE.csv','w')
parse_loc(bs, "browse_loc_FCG_STATE", wr_fcg_state, head_state, sep)
wr_fcg_state.close

## Metro area
head_metro = ["url", "metro_area"]
wr_fcg_metro = open('FCG_METRO.csv','w')
parse_loc(bs, "browse_loc_FCG_METRO", wr_fcg_metro, head_metro, sep)
wr_fcg_metro.close
