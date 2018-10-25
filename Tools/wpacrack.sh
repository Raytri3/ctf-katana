#!/bin/bash
echo " I need a .cap file - where is it?"
read cap
echo ""
echo "I need the SSID name - What is it?"
read SSID
echo""
echo "cracking now, please be patient"
aircrack-ng -e $SSID -w /usr/share/wordlists/wpa.txt "$cap"
