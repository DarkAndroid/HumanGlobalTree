import os 
import requests


listtree = open("prank_tre.ordN.coll",'r')
path3="Replacements.txt"
reps3 = open(path3, "w")

cr=1

while True: 
	print cr
	cr+=1
	read = listtree.readline().strip()
	if read=='':
		break 
	sepread=read.split('	')
	anc=sepread[0]
	first=sepread[1].split(';')[0]
	second=sepread[1].split(';')[1]
	print sepread
	aligment2 = open("ASR.raxml.reduced.prank.anconly.fas",'r')
	aligment1 = open("RefAli.fa",'r')
	if "_" in first:  	
		pr=1
		genome1 = ""
		while True:
	 		name = aligment1.readline().strip()[1:]
			if name == "":
				break
			genome= aligment1.readline().strip()
			if name == first:
				genome1=genome
				break
			pr=pr+1
	else:
		pr=1
		genome1 = ""
		while True:
	 		name = aligment2.readline().strip()[1:]
			if name == "":
				break
			genome= aligment2.readline().strip()
			if name == first:
				genome1=genome
				break
			pr=pr+1

	################################################################################
	aligment2 = open("ASR.raxml.reduced.prank.anconly.fas",'r')
	aligment1 = open("RefAli.fa",'r')
	if "_" in second:
		pr=1
		genome2 = ""
		while True:
	 		name = aligment1.readline().strip()[1:]
			if name == "":
				break
			genome= aligment1.readline().strip()
			if name == second:
				genome2=genome
				break
			pr=pr+1
	else:
		pr=1
		genome2 = ""
		while True:
	 		name = aligment2.readline().strip()[1:]
			if name == "":
				break
			genome= aligment2.readline().strip()
			if name == second:
				genome2=genome
				break
			pr=pr+1   
	length=len(genome1)
	if genome1 == genome2:
		print "SKIP"
	else:
		if len(genome1) == len(genome2):
			print "EQUAL"
		else:
			print "NOT EQUAL"
		for cur in range(length):
			if genome1[cur] != genome2[cur]:
				print "YEAH! %s %s" % (genome1[cur],genome2[cur])
				reps3.write("%s;%s;%s;%s;%s\n" % (first,second,cur,genome1[cur],genome2[cur]))