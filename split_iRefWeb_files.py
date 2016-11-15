# written to split the main file into smaller chuncks for parsing 
# and output
# written 11-11-16, JLW

import csv, os
import numpy as np

f = '9606.mitab.04072015.txt'
d = [l for l in open(f,'rU').readlines()]
headers=d[0]
d.remove(headers)

num_lines = 100000
fcount = float(len(d))/num_lines

for f in np.arange(fcount):
	outf=open('iRef_f'+str(f)+'.txt','w')
	outf.write(headers)
	strt=int(0+(f*num_lines))
	stp=int(f*num_lines+num_lines)
	if f==fcount-1:
		dset=d[strt:]
	else:
		dset=d[strt:stp]
	for l in dset:
		outf.write(l)
	outf.close()

	

	
