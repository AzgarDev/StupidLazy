#!/bin/usr/python
# -*- coding: utf-8 -*-

import sys
import os
import time
import subprocess
import shlex
from pathlib import Path
import colorama
from colorama import Fore, Back, init

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


def option11():
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


def optiona():
    os.system("clear")
    os.system("python page2.py")


def menua():
    try:
        wmenu = raw_input(RED + "You want to go back to the main menu? yes/no : " + RESET)
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
            

def grepno():
    os.system("clear")
    print("ERROR rockyou.txt NOT FOUND!")
    grepa = raw_input("You want to extract rockyou.txt.gz? yes/no : ")
    if grepa == "yes":
        print("EXTRACTING ROCKYOU.TXT")
        os.system("gzip -d /usr/share/wordlists/rockyou.txt.gz")
        time.sleep(10)
        print("DONE")
        menua()
    elif grepa == "no":
        menua()


RED = '\033[31m'
RESET = '\033[0m'
colorama.init(autoreset=True)

try:
    os.system('clear')
    os.system('figlet STUPID LAZY')
    print("\nMADE BY AZGARD...")
    print("1 -- START WIRESHARK           2 -- START APACHE2")
    print("3 -- START TOR SERVICE         4 -- GREP SOMETHING ON ROCKYOU.TXT")
    print("5 -- CHANGE MAC                6 -- RETRIEVE ORIGINAL MAC ADDRESS")
    print("7 -- SCAN A HOST WITH NMAP     8 -- IFCONFIG")
    print("9 -- USE NMAPer !NEW!         10 -- UPDATE")
    print("11 -- CREDITS                  0 -- LEAVE")
    print("")
    print("                 100 -- NEXT PAGE                        ")
    choose = input("\nSelect one option: ")

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
        try:
            kek = open("/usr/share/wordlists/rockyou.txt")
        except IOError:
            grepno()
        finally:
            kek.close()
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
        os.system("python UPDATE.py")
        
    elif choose == 11:
        option11()
        menua()

    elif choose == 0:
        os.system('clear')
        os.system('figlet Bye!')

    elif choose == 100:
        optiona()

    else:
        print(Fore.RED + "\nThis option does not exist !")
        menua()
        
except Exception:
    print(Fore.RED + "\nThis option does not exist !")
    menua()

except NameError:
    print(Fore.RED + "\nThis option does not exist !")
    menua()

except KeyboardInterrupt:
    os.system("clear")
    os.system("figlet Bye!")
    time.sleep(0.001)
    sys.exit()
