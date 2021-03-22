import os 

import requests

import urllib2
from bs4 import BeautifulSoup

src = open("ReplacementsTrueNOgaps.txt",'r')

path3="ReplacementsTrueNOgapsWithoutN.txt"
reps3 = open(path3, "w")

while True: 

	read = src.readline().strip()
	if read=='':
		break
	
	sep=read.split(";")

	if sep[6]!="-" and sep[9]!="N":

		reps3.write ("%s\n" % (read))