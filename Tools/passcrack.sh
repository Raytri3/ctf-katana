#!/bin/bash
echo "Where is the hash file?"
read hashfile
echo ""
x=`echo $[ 1 + $[ RANDOM % 10 ]]`
echo "Running from bash you may not get instant statistics by hitting enter but it is running. To get updates you can  tail the session"$x" log file."
echo "If there are any errors you can run the following..."
echo "john --session=session$x --wordlist=/usr/share/wordlists/rockyou.txt --rules $hashfile &"
john --session=session$x --wordlist=/usr/share/wordlists/rockyou.txt --rules $hashfile &
