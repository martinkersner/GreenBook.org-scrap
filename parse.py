#!/usr/bin/python

################################################################################
# Parsing functions used to scrap GreenBook.org
#
# @author       Martin Kersner
# @email        m.kersner@gmail.com
# @date         19/03/2014
# @last_update  19/03/2014
################################################################################

################################################################################
# Adds header inserted as parameter list to csv file 
# @param  wr  writer csv
# @param  hd  header of csv
# @param  sp separator
################################################################################
def add_header(wr, hd, sp):
  for i in hd:
    if (hd[len(hd)-1] == i):
      wr.write(i + "\n")
    else:
      wr.write(i + sp)

################################################################################
# Parses MARKET RESEARCH SPECIALTIES from homepage
# @param  bs  BeautifulSoup
# @param  tp  type of Specialties
# @param  wr  writer csv
# @param  hd  header of csv
# @param  sp separator
################################################################################
def parse_mrsid(bs, tp, wr, hd, sp):
  add_header(wr, hd, sp)

  ## filling the content
  for i in bs.find(id="searchSpecialties").find(id=tp).find_all("li"):
    ct = i.parent.parent.find_previous_sibling("div").contents[1].contents[1].strip()
    wr.write(i.a.get("href") + sp + ct  + sp + i.a.string + "\n")

################################################################################
# Parses LOCATION from homepage
# @param  bs  BeautifulSoup
# @param  tp  type of Specialties
# @param  wr  writer csv
# @param  hd  header of csv
# @param  sp separator
################################################################################
def parse_loc(bs, tp, wr, hd, sp):
  add_header(wr, hd, sp)

  for i in bs.find(id=tp).find_all("a"):
    wr.write(i.get("href") + sp + i.string + "\n")
