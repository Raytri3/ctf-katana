#!/usr/bin/pyhton 

# program to analyzing white space in a file to see if it contains anything
import re 

# read the file - in this case secret.c
h = open ('secret.c')
c = [ x[:-1] for x in h.readlines()]
h.close()

flag=''
for line in c:
	num = re.findall(r"(\s*)",line)
	if num:
		#converting the spoaces to 1s and 0s
		#try reversing this if it doesn't work
		binnum = ''.join(num).replace(' ','0').replace('\t','1')
		num = int(''.join(num).replace(' ','0').replace('\t','1'),2)
		#check if the number above is ascii range
		print "Analyzing the white spaces..."
		print "The binary is:" 
		print binnum
		print "Convert to decimal is:"
		print num
		if num in range(255):
			print "Trying to convert to ascii:"
			flag += chr(num)
	print flag
