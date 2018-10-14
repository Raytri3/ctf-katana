#!/usr/bin/env python

#program to compare 2 files and find if there are similar characters
f1 = open("col3")
with open("col8") as fh:
	sum = 0
	count = 0
	max=0
	for line in fh:
		count += 1
		sum += float(line)
		num =float (line)
		if (max<num):
			max =num
	avg=sum/count
print avg
print max
	
