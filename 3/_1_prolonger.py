import os 

listtree = open("prank_tre.ordN.coll",'r')

path4="hyperlist.csv"
reps4 = open(path4, "w")

files=os.listdir("Neighbors")

for f in files:
	fi=f[:-4].split("__")
	print fi
	reps4.write("%s;%s\n" % (fi[0],fi[1]))
files=os.listdir("Neighbors_prolong")

for f in files:
	fi=f[:-4].split("__")
	print fi
	reps4.write("%s;%s\n" % (fi[0],fi[1]))

reps4.close()

cr=1

while True: 
	print cr
	cr+=1
	skip=False
	read = listtree.readline().strip()
	if read=='':
		break
	sepread=read.split('	')
	anc=sepread[0]
	first=sepread[1].split(';')[0]
	second=sepread[1].split(';')[1]
	print sepread
	hlist = open("hyperlist.csv",'r')
	while True: 
		lread = hlist.readline().strip()
		if lread=='':  
			break
		if lread==first+";"+second:  
			skip=True
			break
	if skip:
		break
	reps4 = open(path4, "a")
	reps4.write("%s;%s\n" % (first,second))
	reps4.close()
	print "%s  %s" % (first,second)
	path3="Neighbors_prolong/%s__%s.csv" % (first,second)
	reps3 = open(path3, "w")
	ancali = open("ASR.raxml.reduced.prank.anconly.fas",'r')
	pr=1
	ancgenome = ""
	while True:
		name = ancali.readline().strip()[1:]
		if name == "":	
			break
		genome = ancali.readline().strip()
		if name == anc:
			ancgenome=genome
			break
		pr=pr+1   

	#### FIRST with Ancestor
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
	length=len(ancgenome)
	if ancgenome == genome1:
		print "SKIP"
	else:
		if len(ancgenome) == len(genome1):
			print "EQUAL"
		else:
			print "NOT EQUAL"
		for cur in range(length):
			if ancgenome[cur] != genome1[cur]:
				if len(ancgenome[cur:])!=1:
					print "YEAH! %s %s" % (ancgenome[cur],genome1[cur])
					reps3.write("%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (anc,first,cur,ancgenome[cur-1],ancgenome[cur],ancgenome[cur+1],genome1[cur-1],genome1[cur],genome1[cur+1]))
				else:
					print "YEAH! %s %s" % (ancgenome[cur],genome1[cur])
					reps3.write("%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (anc,first,cur,ancgenome[cur-1],ancgenome[cur],ancgenome[0],genome1[cur-1],genome1[cur],genome1[0]))
	if ancgenome == genome2:
		print "SKIP"
	else:
		if len(ancgenome) == len(genome2):
			print "EQUAL"
		else:
			print "NOT EQUAL"
		for cur in range(length):
			if ancgenome[cur] != genome2[cur]:
				if len(ancgenome[cur:])!=1:
					print "YEAH! %s %s" % (ancgenome[cur],genome2[cur])
					reps3.write("%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (anc,second,cur,ancgenome[cur-1],ancgenome[cur],ancgenome[cur+1],genome2[cur-1],genome2[cur],genome2[cur+1]))
				else:
					print "YEAH! %s %s" % (ancgenome[cur],genome2[cur])
					reps3.write("%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (anc,second,cur,ancgenome[cur-1],ancgenome[cur],ancgenome[0],genome2[cur-1],genome2[cur],genome2[0]))