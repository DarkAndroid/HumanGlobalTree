import os 

listtree = open("prank_tre.ordN.coll.pathS",'r')

cr=1

while True: 
	skip=False

	print cr
	
	read = listtree.readline().strip()
	if read=='':
		break

	hread=read.split('	')
	print hread

	try:
		sepread=hread[1].split('__')
	except:
		print "NO HAPLO"
		continue

	path3="Haplo/%s_%s.csv" % (cr,hread[0])
	reps3 = open(path3, "w")

	for pair in range(len(sepread)-1):
 
		first=sepread[pair]
		second=sepread[pair+1]

		path4="FilledN/%s__%s.csv" % (first,second)
		reps4 = open(path4, "r")

		while True: 

			readP = reps4.readline().strip()
			if readP=='':
				break

			reps3.write("%s\n" % (readP))

	cr+=1