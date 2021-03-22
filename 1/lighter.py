import os 
import requests

src = open("refgenes.gb.gff",'r')
path3="refgenes.gb.gff.Truncated"
reps3 = open(path3, "w")

while True: 

	read = src.readline().strip()
	if read=='':
		break
	
	sep=read.split("	")
	 
	if  sep[2]!="STS" and sep[2]!="CDS" and sep[2]!="gene" and sep[2]!="exon" and sep[2]!="region":
		print sep[2]+" "+sep[3]+" "+sep[4]

		reps3.write ("%s	%s	%s	%s	%s	%s	%s	%s\n" % (sep[0],sep[1],sep[2],sep[3],sep[4],sep[5],sep[6],sep[7]))