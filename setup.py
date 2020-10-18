#!/usr/bin/python

import sys
import os
import subprocess
import time

try:
	lol = open("/usr/local/bin/stupidlazy")
	lol.close()

	os.system("clear")
	print("Really?")
	time.sleep(1)
	os.system("clear")
	print("Why the heck you want to run setup again?")
	sys.exit()
except IOError:
	os.system("clear")
	print("Installing...")
	time.sleep(1)
	os.system("sudo apt-get install xterm -y")
	os.system("sudo apt-get install figlet")
	os.system("sudo apt-get install python3-pip")
	os.system("sudo apt-get install python-pip")
	os.system("sudo python pip install colorama")
	os.system("sudo python pip3 install colorama")
	os.system("clear")
	subprocess.Popen("mkdir /usr/share/stupidlazy/;cp -rf * /usr/share/stupidlazy/", shell=True).wait()
	filewrite = open("/usr/local/bin/stupidlazy", "w")
	filewrite.write("#!/bin/sh\ncd /usr/share/stupidlazy\npython stupidlazy.py")
	filewrite.close()
	subprocess.Popen("chmod +x /usr/local/bin/stupidlazy", shell=True).wait()
