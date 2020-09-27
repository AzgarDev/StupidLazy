import sys
import os
import time
import shlex

def option1():
    n1 = os.popen("nmap %s"%ip)
    os.system('clear')
    print(n1.read())
    
def option2():
    n2 = "nmap -p %s %s"%(port, ip1)
    n3 = os.popen(n2)
    os.system('clear')
    print(n3.read())


def option3():
    n4 = os.popen('nmap -O -v %s | grep "OS details: "'%ip2)
    os.system('clear')
    print(n4.read())


def option4():
    n5 = os.popen('nmap -sS -O %s'%ip3)
    os.system('clear')
    print(n5.read())

def menua():
    try:
        menu = raw_input("You want to go back to the menu? yes/no : ")
        if menu == "yes":
            os.system("python NMAPer.py")
        elif menu == "no":
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
    os.system('figlet NMAPer')
    print("\n1 -- HOST PORT DISCOVERY SCAN         2 -- SPECIFIC PORT HOST SCAN")
    print("\n3 -- OS HOST DISCOVERY                4 -- STEALTH HOST PORT AND OS DISCOVERY")
    print("\n5 -- GO BACK TO STUPIDLAZY")
    print("")
    escolha = input("Select one of the options: ")

    if escolha == 1:
        ip = raw_input("Host: ")
        option1()
        menua()
            
    elif escolha == 2:
        ip1 = raw_input("Host: ")
        port = input("Port : ")
        option2()
        menua()
        
    elif escolha == 3:
        ip2 = raw_input("Host: ")
        option3()
        menua()
        
    elif escolha == 4:
        ip3 = raw_input("Host: ")
        option4()
        menua()
        
    elif escolha == 5:
        os.system("python stupidlazy.py")
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
    sys.exit()
