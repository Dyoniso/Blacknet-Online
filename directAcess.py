import sys
import os
import time
if sys.version_info.major < 3:
    print("BlackNet supports only Python3. Run the application in Python3 environment.")
    exit(0)
from core.blackcore import *

def main():
	banner()
	print("")
	print(red+"[!] "+white+"Direct Mode")
	print("")
	theLoop()
		
		
if __name__ == "__main__":
	main()
	

