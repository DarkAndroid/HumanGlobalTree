import os 

path3="Comp.txt"
reps3 = open(path3, "w")

aligment1 = open("Reference.fa",'r')
aligment2 = open("TrueRef.fa",'r')

genome1= aligment1.readline().strip()
genome2= aligment2.readline().strip()

j=0
a=0

for i in range(len(genome1)): 
	if genome1[i] == genome2[j].upper():
		a=0
		genes = open("refgenes.gb.gff.Truncated",'r')
		while True:
			read = genes.readline().strip()
			if read=='':
				print "Cool! %s %s %s %s" % (i,j,genome1[i],genome2[j].upper())
				reps3.write("%s;%s;%s;%s;0;null\n" % (i,j,genome1[i],genome2[j].upper()))   
				break	  
			sepread=read.split('	')
			if (j+1>=int(sepread[3])) and (j+1<=int(sepread[4])):
				print "Cool! %s %s %s %s" % (i,j,genome1[i],genome2[j].upper())
				reps3.write("%s;%s;%s;%s;0;%s\n" % (i,j,genome1[i],genome2[j].upper(),sepread[2]))   
				break			
		j+=1
	else:
		a+=1
		print "Gap! %s %s %s _" % (i,j-1,genome1[i])
		reps3.write("%s;%s;%s;_;%s;None\n" % (i,j-1,genome1[i],a))