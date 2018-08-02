#
# tsvdro: reference implementation for data rich tab separated value objects
#
# Jed Dobson (james.e.dobson@dartmouth.edu)
# Dartmouth College
# http://www.dartmouth.edu/~jed

import numpy as np
import platform
import sys, os
import time
import json

# build the basic header
def build_header():
   header = dict()

   # version number is a string
   header['tsvdro_ver']  = "1.0"

   # build workflow section
   header['workflow'] = dict()
   header['workflow']['created_date'] = time.strftime("%Y-%m-%d %H:%M")
   header['workflow']['created_by'] = "tsdro_reference_implementation"
   header['workflow']['created_system'] = platform.node()
   header['workflow']['vocab_count'] = ""
   header['workflow']['token_count'] = ""

   # build bibliographic section
   header['bibliographic_data'] = dict()
   header['bibliographic_data']['author_name'] = ""
   header['bibliographic_data']['title'] = ""
   header['bibliographic_data']['volumes'] = ""
   header['bibliographic_data']['pages'] = ""
   header['bibliographic_data']['publication_date'] = ""
   header['bibliographic_data']['publisher'] = ""
   header['bibliographic_data']['publisher_location'] = ""
   header['bibliographic_data']['file_uri'] = ""

   return(header)


# function to load a file
def load(filename):
   ''' Load DRO file with the supplied filename
   Returns TSVDRO object
   '''

   try:
      f = open(filename)
   except NameError:
      print('Missing filename')
      return
   except FileNotFoundError:
      print('Cannot locate file:',filename)
      return

   # default format is JSONified data rich object
   # try to read JSON data

   try:
       file_object = json.load(f)

   #
   # If read fails, try to read as plain text
   # 
 
   except json.decoder.JSONDecodeError:

       # assume TSV file
       import csv

       # we will need to construct some data
       print('Not in DRO format: converting')

       tsvdro_object = dict()

       tsv_data = dict()
       with open(filename) as input:

           input = csv.reader(input, delimiter='\t')
           for row in input:
              # add data as dict
              # and only if we have two colums of data
              if len(row) == 2:
                  tsv_data[row[0]] = row[1]
              #tsv_data.append(row)

       tsvdro_object['data'] = tsv_data

       # construct a header
       header = build_header()
       tsvdro_object['header'] = header

       return(tsvdro_object)

   # read the JSON object and return
   tsvdro_object = file_object
   return(tsvdro_object)

def save(object,filename):
   ''' Saves DRO object with the supplied filename
   '''

   with open(filename, "w") as f:
      json.dump(object, f)
   return
