import os 

listtree = open("iqtree_tre.ordN.coll.pathS",'r') # Tree in haplo-chains-form

path4="hyperlist.csv"
reps4 = open(path4, "w")

files=os.listdir("Neighbors")

for f in files:

	fi=f[:-4].split("__")
	print fi
	reps4.write("%s;%s\n" % (fi[0],fi[1]))

reps4.close()

cr=1

while True: 

	skip=False

	print cr
	cr+=1
	
	read = listtree.readline().strip()
	if read=='':
		break
	
	hread=read.split('	')
	print hread

	try:
		sepread=hread[1].split('__')
	except:
		print "NO HAPLO"

	for pair in range(len(sepread)-1):

		first=sepread[pair]
		second=sepread[pair+1]

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

		path3="Neighbors/%s__%s.csv" % (first,second)
		reps3 = open(path3, "w")

		#### FIRST with Ancestor
		aligment2 = open("ASR.raxml.reduced.prank.anconly.fas",'r') # Aligments of internal branches
		aligment1 = open("RefAli.fa",'r') # Reference genome in aligment

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
		aligment2 = open("ASR.raxml.reduced.prank.anconly.fas",'r') # Aligments of internal branches
		aligment1 = open("RefAli.fa",'r') # Reference genome in aligment

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

				if genome1[cur] != genome2[cur] and genome1[cur]!="-" and genome2[cur]!="-" and genome1[cur]!="N" and genome2[cur]!="N":

					if len(genome1[cur:])!=1:

						print "YEAH! %s %s" % (genome1[cur],genome2[cur])
						reps3.write("%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (first,second,cur,genome1[cur-1],genome1[cur],genome1[cur+1],genome2[cur-1],genome2[cur],genome2[cur+1]))

					else:

						print "YEAH! %s %s" % (genome1[cur],genome2[cur])
						reps3.write("%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (first,second,cur,genome1[cur-1],genome1[cur],genome1[0],genome2[cur-1],genome2[cur],genome2[0]))