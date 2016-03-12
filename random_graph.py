#Written to test_graph1
from random import randrange as r
def generate(n=10, m=18):
	f = open('test_graph1' ,'w')
	f.write(str(n)+' '+str(m)+'\n')
	for i in range(m):
		u = r(1,n+1)
		v = r(1,n+1)
		f.write(str(u)+' '+str(v)+'\n')

	f.close()

generate()