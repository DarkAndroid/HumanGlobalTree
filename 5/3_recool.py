import os 

src = open("fulllist.csv",'r')

path3="fulltree.csv"
reps3 = open(path3, "w")

while True: 

	read = src.readline().strip()
	if read=='':
		break
	
	sep=read.split(";")

	reps3.write ("%s;%s;%s;%s;%s;%s;%s;%s\n" % (sep[0],sep[1],sep[2],sep[3],sep[5],sep[4],sep[6],sep[7]))