import os 

folder="Neighbors"
files=os.listdir(folder)
prepath=(folder+"/")

for f in files:
	print f
	listtreeIn = open(prepath+f,'r')
	listtreeOut = open("FilledN/"+f,'w')
	cr=1

	while True: 
		print cr
		cr+=1
		
		read1 = listtreeIn.readline().strip()
		if read1=='':
			break
		
		s1=read1.split(';')
		comp = open("Comp.txt",'r')

		while True: 

			read2 = comp.readline().strip()
			if read2=='':
				break
			
			s2=read2.split(';')

			if s2[0]==s1[2]:

				listtreeOut.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (s1[0],s1[1],s1[2],  s2[0],s2[1],  s1[3],  s1[4],  s1[5],	 s1[6],  s1[7], s1[8],   s2[2],s2[3],s2[4],s2[5]))