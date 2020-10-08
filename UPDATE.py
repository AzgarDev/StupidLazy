import os
import time
import sys

class cd:
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)




try:
	os.system("clear")
	os.system('figlet LAZY UPDATER')
	print("")
	update = raw_input("You want to update stupidlazy and NMAPer? yes/no: ")

	if update == "yes":
		print("GIT CLONING...")
		os.system("git clone https://github.com/AzgarDev/StupidLazy.git")
		time.sleep(5)
		print("REMOVING OLD VERSIONS.")
		os.system("rm -rf stupidlazy.py")
		os.system("rm -rf NMAPer.py")
		os.system("rm -rf page2.py")
		time.sleep(0.5)
		print("COPING NEW FILES")
		with cd("StupidLazy"):
		    os.system("cp stupidlazy.py ../")
		    time.sleep(0.5)
		    os.system("cp NMAPer.py ../")
		    time.sleep(0.5)
		    os.system("cp page2.py ../")

		os.system("cd ..")
		os.system("rm -rf StupidLazy")
		print("DONE")
		sys.exit()
	if update == "no":
		os.system("python stupidlazy.py")
		
	else:
	    print("Please enter a valid value.")
	    time.sleep(2)
	    os.system("python UPDATE.py")
	    
except Exception:
	print("Please enter a valid value.")
	time.sleep(2)
	os.system("python UPDATE.py")
except KeyboardInterrupt:
    os.system("python stupidlazy.py")
