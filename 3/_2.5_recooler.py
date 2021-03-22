import os 

folder="FilledN"
files=os.listdir(folder)
prepath=(folder+"/")

for f in files:
	print f
	listtreeIn = open(prepath+f,'r')
	listtreeOut = open("Filled5/"+f,'w')
	first=f[:-4].split("__")[0]
	second=f[:-4].split("__")[1]

	#### FIRST with Ancestor
	aligment2 = open("ASR.raxml.reduced.prank.anconly.fas",'r')
	aligment1 = open("RefAli.fa",'r')
	if "_" in first:
		pr=1
		genome1 = ""
		while True:
			name = aligment1.readline().strip()[1:]
			if name == "":
				print "END"	
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
	cr=1
	while True: 
		print cr
		cr+=1
		read1 = listtreeIn.readline().strip()
		if read1=='':
			break
		s1=read1.split(';')
		listtreeOut.write("%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (s1[0],s1[1],s1[2]   ,s1[4],	  genome1[int(s1[2])-2:int(s1[2])+3],	 genome2[int(s1[2])-2:int(s1[2])+3],	 s1[11],s1[12],s1[14]))