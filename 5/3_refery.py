import os 

listtree = open("ReplacementsNOgaps.txt",'r')

path3="ReplacementsTrueNOgaps.txt"
reps3 = open(path3, "w")

reps3.write("first;second;position;pos_ref_in_ali;pos_ref_gb;left_from_neighbor;nuc_from;right_from_neighbor;left_to_neighbor;nuc_to;right_to_neighbor;nuc_ref_in_ali;nuc_ref_gb;shift_from_last_ref_pos;gene_info\n")

cr=1

while True: 

	print cr
	cr+=1
	
	read1 = listtree.readline().strip()
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

			reps3.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (s1[0],s1[1],s1[2],s2[0],s2[1],  s1[3],  s1[4],  s1[5],	 s1[6],  s1[7], s1[8],   s2[2],s2[3],s2[4],s2[5]))