#!/usr/bin/python

###############################################################################
# Parsing functions used to scrap GreenBook.org
#
# @author       Martin Kersner
# @email        m.kersner@gmail.com
# @date         19/03/2014
# @last_update  22/03/2014
###############################################################################

import sys

###############################################################################
# Adds header inserted as parameter list to csv file 
# @param  wr  writer csv
# @param  hd  header of csv
# @param  sp separator
###############################################################################
def add_header(wr, hd, sp):
  for i in hd:
    if (hd[len(hd)-1] == i):
      wr.write(i + "\n")
    else:
      wr.write(i + sp)

###############################################################################
# Parses MARKET RESEARCH SPECIALTIES from homepage
# @param  bs  BeautifulSoup
# @param  tp  type of Specialties
# @param  wr  writer csv
# @param  hd  header of csv
# @param  sp separator
###############################################################################
def parse_mrsid(bs, tp, wr, hd, sp):
  add_header(wr, hd, sp)

  ## filling the content
  for i in bs.find(id="searchSpecialties").find(id=tp).find_all("li"):
    ct = i.parent.parent.find_previous_sibling("div").contents[1].contents[1].strip()
    write_csv(wr, [i.a.get("href"), ct, i.a.string], sp)

###############################################################################
# Parses LOCATION from homepage
# @param  bs  BeautifulSoup
# @param  tp  type of Specialties
# @param  wr  writer csv
# @param  hd  header of csv
# @param  sp separator
###############################################################################
def parse_loc(bs, tp, wr, hd, sp):
  add_header(wr, hd, sp)

  ## filling the content
  for i in bs.find(id=tp).find_all("a"):
    write_csv(wr, [i.get("href"), i.string], sp)

###############################################################################
# Prints continually strings from list to csv file using sp separator
# @param  wr  writer csv
# @param  ls  list of items to print
# @param  sp  separator
###############################################################################
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

###############################################################################
# Tries to open a file for reading
# @param  nm  name of file to open
# @param  md  mode of opening
###############################################################################
def open_file(nm, md):
  try:
    return open(nm, md)
  except IOError:
    print >> sys.stderr, "Oops, " + nm + " probably does not exist!"
    print >> sys.stderr, "Exiting."
    exit()

###############################################################################
# Gets telephone from detail of company
# @param  bs  BeautifulSoup
###############################################################################
def get_telephone(bs):
  dd = bs.find_all("dd")
  for i in dd:
    itemprop = i.get("itemprop")

    if itemprop == "telephone" and len(i.string.strip()) != 0:
      telephone = i.string.strip()
      break

  return telephone

###############################################################################
# Gets email and website from detail of company
# @param  bs  BeautifulSoup
###############################################################################
def get_email_website(bs):
  em = bs.find_all("a")
  for i in em:
    if i.get("itemprop") == "email":
      email = i.string.strip()
    else:
      if i.get("itemprop") == "url":
        website = i.string.strip()

  return email, website

###############################################################################
# Gets address items from detail of company
# @param  bs  BeautifulSoup
###############################################################################
def get_address(bs):
  ad = {}
  # filling dict with empty strings
  ad["streetAddress"] = ""
  ad["addressLocality"] = ""
  ad["addressRegion"] = ""
  ad["postalCode"] = ""
  ad["addressCountry"] = ""

  adrs = bs.find_all("address")
  for i in adrs:
    itemprop = i.get("itemprop")

    if itemprop == "address":
      spn = i.find_all("span")
      for k in spn:
        itemprop2 = k.get("itemprop")

        if itemprop2 is not None:
          ad[itemprop2] = k.string.strip()

  return ad
