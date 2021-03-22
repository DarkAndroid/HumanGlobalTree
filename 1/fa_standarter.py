#coding=utf8

import os
import sqlite3
import sys, string
import shutil


pgen_path = 'ASR.raxml.reduced_NC_012920.1.fas'
pgen = open(pgen_path,'r')
reps3 = open('RefAli.fa', "w")

pr=1
genome = ""

while True:
	print pr
	row = pgen.readline().strip()
	if row == "":
		if genome != "":
			reps3.write("%s\n" % (genome))		
		break
	if row[0] == ">":
		name = row.split(" ")[0]
		if genome != "":
			reps3.write("%s\n" % (genome))
		genome = ""
		reps3.write("%s\n" % (name))
	else:
		genome = genome+row.upper()
	pr=pr+1