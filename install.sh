#!/bin/bash

clear
echo "Installing..."
sleep 1
apt-get install xterm
apt-get install figlet
apt-get install python3-pip
apt-get install python-pip
pip install colorama
clear
chmod +x stupidlazy.py
chmod +x NMAPer.py
chmod +x page2.py
chmod +x UPDATE.py
clear
echo "Done"
python stupidlazy.py
