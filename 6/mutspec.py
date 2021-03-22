import os 

src = open("fulltree.csv",'r')

path3="mutspec_pairs.csv"
reps3 = open(path3, "w")

path4="mutspec_sum.txt"
reps4 = open(path4, "w")

src.readline()

at=0
ag=0
ac=0
ta=0
tg=0
tc=0
ga=0
gt=0
gc=0
ca=0
ct=0
cg=0

atsum=0
agsum=0
acsum=0
tasum=0
tgsum=0
tcsum=0
gasum=0
gtsum=0
gcsum=0
casum=0
ctsum=0
cgsum=0


reps3.write ("first;second;at;ag;ac;ta;tg;tc;ga;gt;gc;ca;ct;cg")

lastpair=""

while True: 

	read = src.readline().strip()
	if read=='':
		break
	
	sep=read.split(";")


   
	pair=sep[0]+";"+sep[1]

	if pair!=lastpair:

		reps3.write ("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (lastpair,at,ag,ac,ta,tg,tc,ga,gt,gc,ca,ct,cg))

		at=0
		ag=0
		ac=0
		ta=0
		tg=0
		tc=0
		ga=0
		gt=0
		gc=0
		ca=0
		ct=0
		cg=0


	if sep[4][2]=="A" and sep[5][2]=="T":
		at+=1
		atsum+=1

	elif sep[4][2]=="A" and sep[5][2]=="G":
		ag+=1
		agsum+=1	 

	elif sep[4][2]=="A" and sep[5][2]=="C":
		ac+=1
		acsum+=1

	elif sep[4][2]=="T" and sep[5][2]=="A":
		ta+=1
		tasum+=1   

	elif sep[4][2]=="T" and sep[5][2]=="G":
		tg+=1
		tgsum+=1

	elif sep[4][2]=="T" and sep[5][2]=="C":
		tc+=1
		tcsum+=1   
	
	elif sep[4][2]=="G" and sep[5][2]=="A":
		ga+=1
		gasum+=1

	elif sep[4][2]=="G" and sep[5][2]=="T":
		gt+=1
		gtsum+=1	 

	elif sep[4][2]=="G" and sep[5][2]=="C":
		gc+=1
		gcsum+=1

	elif sep[4][2]=="C" and sep[5][2]=="A":
		ca+=1
		casum+=1   

	elif sep[4][2]=="C" and sep[5][2]=="T":
		ct+=1
		ctsum+=1

	elif sep[4][2]=="C" and sep[5][2]=="G":
		cg+=1
		cgsum+=1  


	lastpair=pair



reps4.write ("A to T: %s\n" % atsum)

reps4.write ("A to G: %s\n" % agsum)	

reps4.write ("A to C: %s\n" % acsum)

reps4.write ("T to A: %s\n" % tasum)

reps4.write ("T to G: %s\n" % tgsum)

reps4.write ("T to C: %s\n" % tcsum)
 
reps4.write ("G to A: %s\n" % gasum)

reps4.write ("G to T: %s\n" % gtsum)

reps4.write ("G to C: %s\n" % gcsum)

reps4.write ("C to A: %s\n" % casum)

reps4.write ("C to T: %s\n" % ctsum)

reps4.write ("C to G: %s\n" % cgsum)