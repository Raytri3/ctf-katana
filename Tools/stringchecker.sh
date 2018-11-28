#!/bin/bash
mnums=`cat /home/prickleypaw/CTF/mnums.txt`
for i in /home/prickleypaw/CTF/Challenges/Parsons/*
do 
	echo "testing strings for..."
	echo $i
	
	if /usr/bin/strings $i |grep -iC1 flag >/dev/null; then
  		echo "potential flag found!!!"
  		/usr/bin/strings $i |grep -iC1 flag
  		echo""
  	else
  		echo "No interesting strings found in" $i
	fi

		echo "testing for files in files"
	for m in $mnums
	do
		if /usr/bin/xxd -p $i| grep $m >/dev/null;then
			echo "Possible embedded file with header" $m "in" $i "running foremost to carve it"
			foremost -T -i $i -o carved_$i
	fi
	done
	
	echo ""
done
