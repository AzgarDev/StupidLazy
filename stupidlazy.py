#!/bin/usr/python
# -*- coding: utf-8 -*-

import sys
import os
import time
import subprocess
import shlex

def option1():
    os.popen("wireshark")


def option2():
    os.popen("systemctl start apache2")
    print("APACHE2 SERVICE STARTED...")


def option3():
	os.popen("systemctl start tor")
	print("TOR SERVICE STARTED...")


def option4():
    os.system('cat /usr/share/wordlists/rockyou.txt | grep "%s"'%grep)


def option5():
    os.popen("macchanger -r %s"%interface)


def option6():
    os.popen("macchanger -p %s"%interface2)


def option7():
    n = os.popen('nmap %s'%hostnm)
    os.system('clear')
    print(n.read())
    

def option8():
    i = os.popen('ifconfig')
    os.system('clear')
    print(i.read())
    
    
def option9():
    os.system("clear")
    os.system("python NMAPer.py")


def option10():
    os.system('clear')
    print("MADE BY")
    time.sleep(1)
    os.system('figlet AzgarD')
    time.sleep(3)
    os.system('clear')
    os.system('figlet THANKS')
    time.sleep(0.3)
    os.system('clear')
    os.system('figlet THANKS.')
    time.sleep(0.3)
    os.system('clear')
    os.system('figlet THANKS..')
    time.sleep(0.3)
    os.system('clear')
    os.system('figlet THANKS...')
    time.sleep(0.3)
    os.system('clear')
    os.system('figlet THANKS....')
    os.system('clear')


def menua():
    try:
        wmenu = raw_input("You want to go back to the main menu? yes/no : ")
        if (wmenu == "yes"):
            os.system("python stupidlazy.py")
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
            
            

try:
    os.system('clear')
    os.system('figlet STUPID LAZY')
    print("MADE BY AZGARD...")
    print("\n1 -- START WIRESHARK           2 -- START APACHE2")
    print("\n3 -- START TOR SERVICE         4 -- GREP SOMETHING ON ROCKYOU.TXT")
    print("\n5 -- CHANGE MAC                6 -- RETRIEVE ORIGINAL MAC ADDRESS")
    print("\n7 -- SCAN A HOST WITH NMAP     8 -- IFCONFIG")
    print("\n9 -- USE NMAPer !NEW! ")
    print("\n10 -- CREDITS                   00 -- LEAVE")
    print("")
    choose = input("Select one option: ")

    if choose == 1:
        option1()
        os.system("python stupidlazy.py")

    elif choose == 2:
        option2()
        time.sleep(1.5)
        os.system("python stupidlazy.py")
        
    elif choose == 3:
        option3()
        time.sleep(1.5)
        os.system("python stupidlazy.py")
         
    elif choose == 4:
        grep = raw_input("What you want to grab?: ")
        os.system('clear')
        option4()
        menua()
	    
    elif choose == 5:
        interface = raw_input("Whats your network interface?: ")
        option5()
        print("MAC ADDRESS CHANGED...")
        time.sleep(1.5)
        os.system("python stupidlazy.py")

    elif choose == 6:
        interface2 = raw_input("Whats your network interface?: ")
        option6()
        print("MAC ADDRESS CHANGED...")
        time.sleep(1.5)
        os.system("python stupidlazy.py")
	    
    elif choose == 7:
        hostnm = raw_input("Host: ")
        option7()
        menua()
        
    elif choose == 8:
        option8()
        menua()
        
    elif choose == 9:
        option9()
        
    elif choose == 10:
        option10()
        menua()
	    
    elif choose == 00:
        os.system('clear')
        os.system('figlet Bye!')
    else:
        print("This option does not exist !")
        menua()
        
except Exception:
    print("This option does not exist !")
    menua()

except NameError:
    print("This option does not exist !")
    menua()

except KeyboardInterrupt:
    os.system("clear")
    os.system("figlet Bye!")
    time.sleep(0.001)
    sys.exit()