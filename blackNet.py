import sys
import os
import time
if sys.version_info.major < 3:
    print("BlackNet supports only Python3. Run the application in Python3 environment.")
    exit(0)
from core.blackcore import *

def main():
	try:
		banner()
		print("")
		print("* Select [1] to start blackNet. ")
		print("* Select [2] to start directMode. ")
		print("* Select [3] to Exit. ")
		print("")
		blackInput = input(tag+"blackNet > ")
		if blackInput == "1" or blackInput == "01":
			getCreds()
		elif blackInput == "2" or blackInput == "02":
			print("")
			print(red+"[!] "+white+"Direct Mode")
			print("")
			theLoop()
		elif blackInput == "3" or blackInput == "03":
			exit(0)
	except(KeyboardInterrupt, SystemExit):
		print(tag3+"Tool Interrupted"+"\n")
		exit(0)
		
if __name__ == "__main__":
	main()
	

