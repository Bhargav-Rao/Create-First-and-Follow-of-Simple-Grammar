'''
Exit status - 
0x00	- -> not present
0x01	- Left is terminal
0x02	- Left is null
0x03	- No terminals found
0x04	- RHS Terminals without Productions
'''



import re

chk = 0
grammar = []
nts = set()
ts = set()
dic = dict()


def first(g):
		firstset = set()
		if g in ts:
			firstset.add(g)
		else:
			if '' in dic[g]:
				firstset.add('')
		
			prods = dic[g]
			for i in prods:
				cnt = 0
				for j in i:
					
					if j in ts:					
						firstset.add(j)
						break
					else:
						if (j == g ):
							if ('' in dic[j]):
								continue
							else:
								break
						for k in first(j):
							if not k=='':
								firstset.add(k)
						if not('' in first(j)):
							break
						if j == i[-1]:
							if ('' in first(j)):
								firstset.add('')
		
					
		return firstset

def follow(g):
	followset = set()
	if (g== grammar[0].split('->')[0]):
		followset.add('$')
	for i in grammar:
		rh = i.split('->')
		rh = rh[1]
		if (g in rh):
			#if not(rh[len(rh)-1] == g):
			if (g in rh[:-1]):
				rhsprt = rh.split(g,1)
				rhsprt  =  (rhsprt[1])
				
				for j in rhsprt:
					for k in first(j):
						if not (k == ''):
							followset.add(k)
					if ('' not in first(j)):
						break
				
				cnt = 0
				for j in rhsprt:
					if ('' not in first(j)):
						cnt =1
				if (cnt == 0):
					x = i.split('->')[0]
					if not(g==x):
						try:
							for i in follow (i.split('->')[0]):
								followset.add(i)
						except:
							pass
			if (g == rh[-1]):
				x = i.split('->')[0]
				if not(g==x):
					try:
						for i in follow (x):
							followset.add(i)
					except:
						pass
				
	return followset


def chklftrec():
	return False



def chkgram(grammar):
	for i in grammar:
		if '->' not in i:
			print ("Erreur: Syntax Invalid")
			print ("Exited with status --0x00--")
			return 0
	else:
		split= []
		for i in grammar:
			t = re.search("(.*)->(.*)",i)
			split.append(t.groups())
		lhsnts= set()
		rhs = set()
		for i in split:
	
			for j in i[1]:
				rhs.add (j)	
			if (i[0].isupper()):
				lhsnts.add(i[0])
			elif (i[0] == ''):
				print ("Erreur: Grammar Invalid")
				print ("Exited with status --0x02--")
				return 0
			else:
				print ("Erreur: Grammar Invalid")
				print ("Exited with status --0x01--")
				return 0
		else:
			rhsnts= set()
			rhsts = set()
			for i in rhs:
				if i.isupper():
					rhsnts.add(i)
				else:
					rhsts.add(i)
			#print (rhs)
			#print (rhsnts)
			#print (rhsts)
			#print (lhsnts)
			if len(rhsts) == 0:
				print ("Erreur: Grammar Invalid")
				print ("Exited with status --0x03--")
				return 0
			else:
						 
				for i in rhsnts:
					if i not in lhsnts:
						print ("Erreur: Grammar Invalid")
						print ("Exited with status --0x04--")
						return 0
				else:	
					#global dic
					for i in split:
						values= []
						dic [i[0]] = []
						for j in split:
							k = j[0]
							if i[0] == k:
								dic[i[0]].append(j[1])
	
					#global nts
					for i in lhsnts:
						nts.add(i)
					for i in rhsnts:
						nts.add(i)
					#global ts
					for i in rhsts:
						ts.add(i)
					return 1	

if __name__ == "__main__":
	fp = open ("new.txt")
	fp2 = open("fst.txt",'w')
	fp3 = open("fol.txt",'w')
	fp4 = open("sym.txt",'w')
	for i in fp:
		grammar.append(i.strip('\n'))	
	
	check1 = chkgram(grammar)				
	if check1 == 1:
		check2 = chklftrec()
		if not check2:
			for i in sorted(nts):
				fp2.write(str(first(i))+"\n")
				fp3.write(str(follow(i))+"\n")
				fp4.write(i+"\n")			
				
