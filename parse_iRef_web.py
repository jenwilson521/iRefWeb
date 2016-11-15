# writte to parse the interaction file
# map identifiers
# score - misore?
# written 11-10-16, JLW

import csv, math, pickle
from collections import defaultdict

# define constants for later
(kp,km,kt)=(1,1,1)
bmax = 7 # max number of publications
scv_dic={'MI:0013(biophysical)':1.0,'MI:0090(protein complementation assay)':0.66,'MI:0254(genetic interference)':0.10,'MI:0255(post transciptional interference)':0.10,'MI:0401(biochemical)':1.00,'MI:0428(imaging technique)':0.33,'-':0.05}
gscv_m = sum(scv_dic.keys())
type_dic={'MI:0208(genetic interaction)':0.1,'MI:0403(colocalization)':0.33,'MI:0914(association)':0.33,'MI:0915(physical association)':0.66,'MI:0407(direct interaction)','-':0.05}
gscv_t=sum([1.0,0.33,1.0])

def pub_score(plist):
	pn = len(plist)
	if pn > bmax:
		pn=bmax
	b = bmax
	sp=math.log(pn+1,b+1)
	
	return sp 

def meth_score(mlist):
	s_scores = [scv_dic[s] if s in scv_dic else 0.05 for s in mlist]
	a = sum(s_scores)
	b = a + gscv_m 
	
	sm=math.log(a+1,b+1)
	return sm

def type_score(tlist):
	t_scores = [type_dic[t] if t in type_dic else 0.05 for t in tlist]
	a = sum(t_scores)
	b = a + gscv_t
	st=math.log(a+1,b+1)
	return st	

def miscore(d): # pass the method a dictionary of data for the interaction
	plist = d['pub'] # publication list
	sp = pub_score(plist)

	mlist = d['scvs'] # method list
	sm = meth_score(mlist)

	tlist = d['type']
	st = type_score(tlist)
	
	smi = (kp*sp + km*sm + kt*st)*(1/(kp*km*kt))
	return smi
	

def parse_data(f):
	# method for consolidating data from multiple interactions
	dr = csv.DictReader(open(f,'rU'),delimiter='\t')
	int_data = defaultdict(lambda: defaultdict(list))
	for row in dr:
		# Loop through interaction data and consolidate information for all interactions
		a = row['#uidA']
		b = row['uidB']

		# Get publication data
		pubmeds = row['pmids']
		if '|' in pubmeds:
			pb_split=pubmeds.split('|')
			for p in pb_split:
				int_data[(a,b)]['pub'].append(p)
		else:
			int_data[(a,b)]['pub'].append(pubmeds)

		# Get method data
		methods = row['method'] 
		if '|' in methds:
			md_split=methods.split('|')
			for m in md_split:
				int_data[(a,b)]['scvs'].append(m)
		else:
			int_data[(a,b)]['scvs'].append(methods)
	
		# Get type data
		inttype = row['interactionType']
		int_data[(a,b)]['type'].append(inttype)	

		# check if complex
		if row['edgetype']=='C':
			# do something

		return int_data

def main()
# Start parsing the interaction data
f = '9606.mitab.04072015.txt'
idic=parse_data(f)
for (a,b) in idic.keys():
	smi = miscore(idic[(a,b)])
	# convert a
	# convert b
	outf
	# write to output and close


if __name__==__main__:
	main()
