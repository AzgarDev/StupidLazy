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
	print("A error happend? if yes, contact azgard on github, unfortunely i cannot help you, sorry")
	time.sleep(1)
	print("AzgarD is going to fix for you <3 just contact him on github with max details of the error")
	print("BYE!")
	time.sleep(1)
	sys.exit()
except IOError:
	os.system("clear")
	print("Installing...")
	time.sleep(1)
	os.system("pip install beautifulsoup4")
	os.system("pip install google")
	os.system("sudo apt-get install xterm -y")
	os.system("sudo apt-get install figlet")
	os.system("sudo apt-get install python3-pip")
	os.system("sudo apt-get install python-pip")
	os.system("sudo python pip install colorama")
	os.system("sudo python pip3 install colorama")
	os.system("clear")
	os.system("cp -rf /usr/lib/python3/dist-packages/colorama /usr/lib/python2.7/dist-packages/")
	os.system("cp -rf /usr/lib/python3/dist-packages/colorama-0.4.3.egg-info /usr/lib/python2.7/dist-packages/")
	os.system("cp -rf /usr/lib/python3/dist-packages/requests /usr/lib/python2.7/dist-packages/")
	os.system("cp -rf /usr/lib/python3/dist-packages/requests_file-1.5.1.egg-info /usr/lib/python2.7/dist-packages/")
	os.system("cp -rf /usr/lib/python3/dist-packages/urllib3 /usr/lib/python2.7/dist-packages/")
	os.system("cp -rf /usr/lib/python3/dist-packages/urllib3-1.25.9.egg-info /usr/lib/python2.7/dist-packages/")
	os.system("cp -rf /usr/lib/python3/dist-packages/six.py /usr/lib/python2.7/dist-packages/")
	os.system("cp -rf /usr/lib/python3/dist-packages/six-1.15.0.egg-info /usr/lib/python2.7/dist-packages/")
	os.system("cp -rf /usr/lib/python3/dist-packages/certifi /usr/lib/python2.7/dist-packages/")
	os.system("cp -rf /usr/lib/python3/dist-packages/certifi-2020.6.20.egg-info /usr/lib/python2.7/dist-packages/")
	os.system("cp -rf /usr/lib/python3/dist-packages/idna /usr/lib/python2.7/dist-packages/")
	os.system("cp -rf /usr/lib/python3/dist-packages/idna-2.10.egg-info /usr/lib/python2.7/dist-packages/")
	os.system("clear")
	subprocess.Popen("mkdir /usr/share/stupidlazy/;cp -rf * /usr/share/stupidlazy/", shell=True).wait()
	filewrite = open("/usr/local/bin/stupidlazy", "w")
	filewrite.write("#!/bin/sh\ncd /usr/share/stupidlazy\npython stupidlazy.py")
	filewrite.close()
	subprocess.Popen("chmod +x /usr/local/bin/stupidlazy", shell=True).wait()
