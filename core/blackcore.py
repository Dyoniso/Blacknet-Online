import os
import sys
import time
import telnetlib
import getpass
import urllib.request
import itertools
import threading

red = "\033[0;31m"
white = "\033[0m"
blue = "\033[94m"
green = "\033[92m"
magenta = "\033[1;35;40m"

tag3 = red+"[X] "+white
tag2 = green+"[+] "+white
tag1 = red+"[+] "+white
tag = blue+"[*] "+white

blackNetBanner = "\n"+"""
 ______  __                __      ____  _____        _    
|_   _ \[  |              [  |  _ |_   \|_   _|      / |_  
  | |_) || | ,--.   .---.  | | / ]  |   \ | |  .---.`| |-' 
  |  __'.| |`'_\ : / /'`\] | '' <   | |\ \| | / /__\\| |   
 _| |__) | |// | |,| \__.  | |`\ \ _| |_\   |_| \__.,| |,  
|_______[___]'-;__/'.___.'[__|  \_]_____|\____|'.__.'\__/  

"""    

netZappBanner = blue+"""
  ,.,,,,,,,,,,,.,,,,,
    . .. .  . / ..  .
           , /
         , '/
        , '/
       , '/ _____,
     .'____, '
           /, '
          /, '
         /, '
        / '   
              -> BlackNet >.<
"""

menuopt = """
  Use BlackNet to bring down wifi acess 
  This tool is not responsible for damage to third parties...
  Let´s play
  -> By Dyoniso_
  """

os.system("clear")

os.chdir(r"core/")
os.system("rm -r __pycache__")
os.chdir(r"../")

def reset():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def getCreds(): 
	
	user1 = input(tag1+"Enter your router user: ")
	password1 = getpass.getpass()
	timmer = input(tag1+"Set Timmer: ")
	timmerInt = int(timmer)
	
	if timmerInt >= 8:
		print("")
		print(tag+"Writing data...")
		arqUser = open('data/user.txt', 'w')
		arqUser.write(user1)
		arqUser.close()
		arqPassword = open('data/password.txt', 'w')
		arqPassword.write(password1)
		arqPassword.close()
		arqTimmer = open('data/timmer.txt', 'w')
		arqTimmer.write(timmer)
		arqTimmer.close()
		blackNetWorks()
		theLoop()
	else:
		print(tag3+"the time is less than 8")
		exit(0)
	

def theLoop():
			
	arq3 = open('data/timmer.txt', 'r')
	timmerStr = arq3.read()
	timmer = int(timmerStr)
	
	try:
		def animate():
			for c in itertools.cycle([">"+red+" 0   "+magenta+"#",
			"->"+green+" 0  "+magenta+"#", "-->"+green+" 0 "+magenta+"#",
			"--->"+green+" 0"+magenta+"#", "--->"+red+"  #"]):
				if done == True:
					break
				sys.stdout.write("\r"+tag+"Loading " + c)
				sys.stdout.flush()
				time.sleep(0.1)
			
		while(True):
		
			done = False
			t = threading.Thread(target=animate)
			t.start()
			
			time.sleep(timmer)
			done = True
			blackNetWorks()
				
	except(KeyboardInterrupt, SystemExit):
		print("\n")
		done = True
		exit(0)
	
def blackNetWorks():
	
	try:
		getip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
		print("\n"+tag+green+"Reading "+getip+" Ok!"+white)
	except:
		print(red+" Error!") 
		print(blackNetBanner) 
		print(tag3+"Error to get public ip, rebooting tool...")
		theLoop()
	
	arq1 = open('data/user.txt', 'r')
	arq2 = open('data/password.txt', 'r')
	txtUser = arq1.read()
	txtPassword = arq2.read()
		
	HOST = getip
	user = txtUser
	password = txtPassword
		
	try:
		tn = telnetlib.Telnet(HOST)
		
		sys.stdout.write("\r"+tag+HOST+"/User:"+user+"/Pass:"+password+"    <- "+green+"Connecting.")
		time.sleep(0.5)
		sys.stdout.write("\r"+tag+HOST+"/User:"+user+"/Pass:"+password+"   <-- "+green+"Connecting..")
		time.sleep(0.5)
		sys.stdout.write("\r"+tag+HOST+"/User:"+user+"/Pass:"+password+"  <--- "+green+"Connecting...")
		time.sleep(0.5)
		sys.stdout.write("\r"+tag+HOST+"/User:"+user+"/Pass:"+password+" <---- "+green+"Connected ...")
		time.sleep(0.5)
		sys.stdout.write("\r"+tag+"###.###.###.###"+"/User:"+user+"/Pass:"+password+" <---- "+green+"Connected ###")
		time.sleep(0.5)
		
		tn.read_until(b"login: ")
		tn.write(user.encode('ascii') + b"\n")
		
		if password:
			tn.read_until(b"Password: ")
			tn.write(password.encode('ascii') + b"\n")
			
		print("")
		print(tag+"Rebooting Router...")
		sys.stdout.write(green+"\r000:"+blue+"______________"+red+"#"+blue+"]")
		time.sleep(0.5)
		sys.stdout.write(green+"\r000:"+blue+"_________"+red+"#"+blue+"_____]")
		time.sleep(0.5)
		sys.stdout.write(green+"\r000:"+blue+"_____"+red+"#"+blue+"_________]")
		time.sleep(0.5)
		sys.stdout.write(green+"\r000:"+red+"#"+blue+"______________]")
		time.sleep(0.5)
		sys.stdout.write(green+"\r000:"+blue+"_______________]")
		time.sleep(0.5)
		sys.stdout.write(red+"\r###:")
		time.sleep(0.5)
		tn.write(b"reboot\n")
		tn.write(b"poweroff\n")
		sys.stdout.write("\r"+tag2+"Complete!:~~~~~~")
		time.sleep(0.5)
		print("\n"+tag+"Clearing pycache...")
		try:
			os.chdir(r"core")
			os.system("rm -r __pycache__")
			os.chdir(r"../")
			print(tag2+"Complete!")
		except:
			print(tag3+"Error!")
		time.sleep(0.5)
		
	except:
		print(blackNetBanner) 
		print(tag3+"Fatal Error, rebooting tool...")
		theLoop()
	
	  
def banner():

	print(blackNetBanner) 
	print(menuopt)

def netZapp():

	print(netZappBanner)
	print(red+"[!] "+white+"netZapp ON")
	print("")

	try:
		getip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
		print("\n"+tag+green+"Reading "+getip+" Ok!"+white)
	except:
		print(tag3+"Error to get public ip.")
		exit()

	arq1 = open('data/user.txt', 'r')
	arq2 = open('data/password.txt', 'r')
	txtUser = arq1.read()
	txtPassword = arq2.read()
		
	HOST = getip
	user = txtUser
	password = txtPassword

	try:
		tn = telnetlib.Telnet(HOST)
		
		sys.stdout.write("\r"+tag+HOST+"/User:"+user+"/Pass:"+password+"    <- "+green+"Connecting.")
		time.sleep(0.1)
		sys.stdout.write("\r"+tag+HOST+"/User:"+user+"/Pass:"+password+"   <-- "+green+"Connecting..")
		time.sleep(0.1)
		sys.stdout.write("\r"+tag+HOST+"/User:"+user+"/Pass:"+password+"  <--- "+green+"Connecting...")
		time.sleep(0.1)
		sys.stdout.write("\r"+tag+HOST+"/User:"+user+"/Pass:"+password+" <---- "+green+"Connected ...")
		time.sleep(0.1)
		sys.stdout.write("\r"+tag+"###.###.###.###"+"/User:"+user+"/Pass:"+password+" <---- "+green+"Connected ###")
		time.sleep(0.1)
		
		tn.read_until(b"login: ")
		tn.write(user.encode('ascii') + b"\n")
		
		if password:
			tn.read_until(b"Password: ")
			tn.write(password.encode('ascii') + b"\n")
			
		print("")
		print(tag+"Rebooting Router...")
		sys.stdout.write(green+"\r000:"+blue+"______________"+red+"#"+blue+"]")
		time.sleep(0.3)
		sys.stdout.write(green+"\r000:"+blue+"_________"+red+"#"+blue+"_____]")
		time.sleep(0.3)
		sys.stdout.write(green+"\r000:"+blue+"_____"+red+"#"+blue+"_________]")
		time.sleep(0.3)
		sys.stdout.write(green+"\r000:"+red+"#"+blue+"______________]")
		time.sleep(0.3)
		sys.stdout.write(green+"\r000:"+blue+"_______________]")
		time.sleep(0.3)
		sys.stdout.write(red+"\r###:")
		time.sleep(0.3)
		tn.write(b"reboot\n")
		tn.write(b"poweroff\n")
		sys.stdout.write("\r"+tag2+"Complete!:~~~~~~"+"\n")
		
	except:
		print("\n"+tag3+"Fatal Error, Connection Refused")
		exit()





	


		
	
	




                                       

