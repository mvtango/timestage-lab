#! /usr/bin/python
# coding: utf-8

import argparse
import sys,os
_here=os.path.split(__file__)[0]
import csv
import re
import datetime
import pprint
import locale
import logging
import codecs
import simplejson
from uuid import uuid4
import couchdb


logging.basicConfig(file=sys.stderr,level=logging.DEBUG)
logger=logging.getLogger(__name__)
locale.setlocale(locale.LC_ALL, "de_DE.utf8")

parser = argparse.ArgumentParser(description="couchdb file storer", conflict_handler='resolve')
parser.add_argument('input_file', action="store",nargs="*")

parser.add_argument('-s','--server',action="store",help="URL of Couchdb Name", default="http://localhost:5984", metavar="http://server:port/database")
parser.add_argument('-d','--db',action="store",help="Database name", default="timestage", metavar="DBNAME")
parser.add_argument('-v','--verbose',action="store",help="output debug info",default=False)

args = vars(parser.parse_args())

if __name__== "__main__" : 
	server=couchdb.Server(args["server"])
	database=server[args["db"]]
	for f in args["input_file"] :
		ob=simplejson.load(open(f))
		st=str(uuid4())
		database[st]=ob
		logger.info("%s byte written to %s[%s]" % (len(simplejson.dumps(ob)), args["db"],st))		
