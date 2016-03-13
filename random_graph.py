#Written to test_graph1

from random import randrange as r
import sys

def generate(n=10, m=18, file='test_graph1'):
	f = open(file ,'w')
	f.write(str(n)+' '+str(m)+'\n')
	for i in range(m):
		u = r(1,n+1)
		v = r(1,n+1)
		f.write(str(u)+' '+str(v)+'\n')

	f.close()

if(len(sys.argv)==4):
	n = int(sys.argv[1])
	m = int(sys.argv[2])
	s = sys.argv[3]
	generate(n,m,s)
else:
	generate()