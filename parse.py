#!/usr/bin/python

################################################################################
# Parsing functions used to scrap GreenBook.org
#
# @author       Martin Kersner
# @email        m.kersner@gmail.com
# @date         19/03/2014
# @last_update  20/03/2014
################################################################################

import sys

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
    write_csv(wr, [i.a.get("href"), ct, i.a.string], sp)

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

  ## filling the content
  for i in bs.find(id=tp).find_all("a"):
    write_csv(wr, [i.get("href"), i.string], sp)

################################################################################
# Prints continually strings from list to csv file using sp separator
# @param  wr  writer csv
# @param  ls  list of items to print
# @param  sp  separator
################################################################################
def write_csv(wr, ls, sp):
  ln = len(ls)

  for i in range(0, ln):
    try:
      wr.write(ls[i])
    except UnicodeEncodeError:
      ## solves problems with character character u'\xbb'
      wr.write(ls[i].encode('utf-8'))

    ## prints separator or newline
    if (i == ln-1):
      wr.write("\n")
    else:
      wr.write(sp)

################################################################################
# Tries to open a file for reading
# @param  nm  name of file to open
# @param  md  mode of opening
################################################################################
def open_file(nm, md):
  try:
    return open(nm, md)
  except IOError:
    print >> sys.stderr, "Oops, " + nm + " probably does not exist!"
    print >> sys.stderr, "Exiting."
    exit()
