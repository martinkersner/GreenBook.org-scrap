#!/usr/bin/python

################################################################################
# Scrapping of company GreenBook.org
#
# @author       Martin Kersner
# @email        m.kersner@gmail.com
# @date         21/03/2014
# @last_update  22/03/2014
###############################################################################

from settings import *
from parse import *
import csv
import time
import requests
from bs4 import BeautifulSoup

csv_names = [ 
#    mrsid_1, 
#    mrsid_2, 
#    mrsid_3,
#    mrsid_4,
#    mrsid_5,
#    mrsid_6,

#mrs_ctry,
#    mrs_state,
#    mrs_metro,
#    fcg_ctry,
    fcg_state,
#    fcg_metro
    ]

url = []

for i in csv_names:
  ## process of loading data
  print i

  rd = open_file(i + category + ext, 'r')

  header = True
  for r in csv.reader(rd, delimiter=sep):
    # skip header
    if header:
      header = False
    else:
      url.append(r[2])

  # all url loaded, file can be closed
  rd.close

wr = open_file(detail_company + ext, 'w')
head_det = ["url", "title", "description", "telephone", "email", "website", "streetAddress", "addressLocality", "addressRegion", "postalCode", "addressCountry"]
write_csv(wr, head_det, sep)

## SCRAP
for j in url:
  time.sleep(1)
  print j
  response = requests.get(website + j) 
  html = response.text
  bs = BeautifulSoup(html)

  ## title
  title = bs.h2.string.strip()

  ## description
  description = get_description(bs)

  ## telephone
  telephone = get_telephone(bs)

  ## address
  address = get_address(bs)

  ## email & url
  email, web = get_email_website(bs)

  # print to csv file
  ls = [j, 
        title, 
        description, 
        telephone, 
        email, 
        web,
        address["streetAddress"],
        address["addressLocality"],
        address["addressRegion"],
        address["postalCode"],
        address["addressCountry"]]

  write_csv(wr, ls, sep)

wr.close
