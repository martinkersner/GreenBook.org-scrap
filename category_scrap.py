#!/usr/bin/python

################################################################################
# Scrapping of category list GreenBook.org
#
# @author       Martin Kersner
# @email        m.kersner@gmail.com
# @date         20/03/2014
# @last_update  21/03/2014
###############################################################################

import sys
from settings import *
import csv
import requests
from bs4 import BeautifulSoup
import time
from urlparse import parse_qs, urlparse
from parse import *

## load links to categories
csv_names = [ 
    #mrsid_1, 
    #mrsid_2, 
    mrsid_3
    #mrsid_4,
    #mrsid_5,
    #mrsid_6,
    #mrs_ctry,
    #mrs_state,
    #mrs_metro,
    #fcg_ctry,
    #fcg_state,
    #fcg_metro
    ]

for i in csv_names:
  ## process of scraping
  print i

  rd = open_file(i + ext, 'r')

  url = []
  header = True
  for r in csv.reader(rd, delimiter=sep):
    # skip header
    if header:
      header = False
    else:
      url.append(r[0])

  # all url loaded, file can be closed
  rd.close

  wr = open_file(i + category + ext, 'w')

  # scrap
  for j in url:
    time.sleep(1)
    response = requests.get(website + j) 
    html = response.text
    bs = BeautifulSoup(html)

    # prints info about scraping
    print j

    # add header
    write_csv(wr, ["url", "heading", "link", "telephone", "area"], sep)

    # there are more subpages
    if bs.find(class_="pagination") != None:
      link_sbp = bs.find(class_="pagination").find(class_="pagination").ul.find_all("li")

      # getting the last link item containing number of new urls
      for en in range(0, len(link_sbp)):
        url_sbp = link_sbp[en].a.get("href")

      # parsing url query to get "page" and "rd"
      pr = parse_qs(urlparse(url_sbp).query, keep_blank_values=True)
      last_page = int(pr["page"][0])
      char = pr["rd"][0]

      # adding new subpages
      for page in range(2, last_page+1):
        new_sbp = j + "?page=" + str(page) + "&rd=" + char
        url.append(new_sbp)

    for k in bs.find_all(class_="article-lrg"):
      try:
        heading = k.find(class_="strong").find("b").contents[0]
        link = k.find(class_="strong").find("a").get("href")
        telephone = k.find(class_="article-info").contents[2].strip()
        area = k.find(class_="article-info").contents[4].strip()[0:-2]
      except AttributeError:
        print >> sys.stderr, "Attribute Error: " + j
        continue

      write_csv(wr, [j, heading, link, telephone, area], sep)

  # category is finished
  wr.close
  time.sleep(2)
