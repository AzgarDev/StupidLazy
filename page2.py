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
		print("OPEN A ANOTHER TERMINAL AND SELECT OPTION A4")
		time.sleep(2)
		os.system("clear")
		nc = os.system("nc -l -p %s"%ncl)
		os.system("python page2.py")
	except KeyboardInterrupt:
		print("\nListener stoped...")


def optiona4():
		ncll = raw_input("Want to test connectivity? yes/no : ")
		if ncll == "yes":
			nclll = input("What port you want to connect : ")
			os.system("clear")
			print("Anything you type here, is going to appear on the other terminal")
			xte = 'echo "Anything you type here, is going to appear on the other terminal" | sudo gnome-terminal -x bash -c "nc %s %s" 2> /dev/null'%(host, nclll)
			os.system(xte)
		if ncll == "no":
			optiona44()


def optiona44():
	try:
		hostnc = raw_input("What host you want to connect on your network? : ")
		hostncl = input("What port you want to connect: ")
		print("Anything you type here, is going to appear on the other terminal")
		xte = 'echo "Anything you type here, is going to appear on the other terminal" | sudo gnome-terminal -x bash -c "nc %s %s" 2> /dev/null'%(hostnc, hostncl)
		os.system(xte)
	except:
		print("Select a valid port please")


host = socket.gethostname()
ip = socket.gethostbyname(host)


try:
	os.system("clear")
	os.system("figlet PAGE2")
	print("")
	print("a1 -- START MSFCONSOLE			a2 -- AUTOMATIC UPDATE YOU MACHINE")
	print("a3 -- START LISTENER NETCAT		a4 -- CONNECT TO YOUR NETWORK USING NETCAT")
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

except KeyboardInterrupt:
	os.system("python stupidlazy.py")
