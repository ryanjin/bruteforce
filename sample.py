# -*- coding: utf-8 -*-  
import time
import os
import random


codeLen=4
samp=[]

#基数0-9
for i in range(48,48+10):
	samp.append(chr(i))

#基数A-Z
'''
for i in range(65,65+26):
	samp.append(chr(i))
'''
#基数a-z
for i in range(97,97+26):
	samp.append(chr(i))


print "sample :", samp

#随机变化
def rand(list):
	change=10
	for i in range(change):
		rand1 = random.randint(0,len(list)-1)
		rand2 = random.randint(0,len(list)-1)
		j = list[rand1]
		list[rand1]=list[rand2]
		list[rand2]=j

rand(samp)
print "sample after change :",samp

filename = 'sample.txt'
if os.path.exists(filename):
	print 'WARN ',filename,'exists'
	exit()

output = open(filename,'w')
print 'make file ',filename

tmp=[]
for i in samp:
	tmp.append(i)
for i in range(1,codeLen):
	tmp2=[]
	for j in tmp:
		rand(samp)
		for k in samp:
			tmp2.append(j+k)
	rand(tmp2)
	tmp=tmp2

for i in tmp:
	output.write(i+'\n')

print 'write success, total:',len(tmp)
output.close();

