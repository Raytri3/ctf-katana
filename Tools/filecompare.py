#!/usr/bin/env python

#program to compare 2 files and find if there are similar characters
f1 = open("file1").read()
f2 = open("file2").read()
print len(f1), len(f2)
decoded1 =''
decoded2 =''
decoded3 =''
for i in range(len(f1)):
	if (f1[i]==f2[i]):
		decoded1 +=(f1[i])
	if (f1[i]==f2[i-1]):
		decoded2 +=(f1[i])
print "Printing characters in the same index:"
print decoded1
print "index -1:"
print decoded2



