#!/bin/bash

clear
echo "Installing..."
sleep 1
apt-get install xterm -y
apt-get install figlet -y
apt-get install python3-pip -y
apt-get install python-pip -y
pip install colorama
clear
chmod +x stupidlazy.py
chmod +x NMAPer.py
chmod +x page2.py
chmod +x UPDATE.py
clear
echo "Done"
sleep 2
python stupidlazy.py
