#main.py
import task
import sign
import json
import os

myInfo ={}
if os.path.isfile("/etc/LXH_SignAssist/config.json") ==False:
	if os.path.exists("/etc/LXH_SignAssist") ==False:
		os.mkdir("/etc/LXH_SignAssist")
	os.mknod("/etc/LXH_SignAssist/config.json")
configFile = open("/etc/LXH_SignAssist/config.json","r+")

configData = configFile.read()
 
if configData == "" :
	print("Your config file is empty. Let's make a set up.")
	myInfo["BDUSS"] = input("Your BDUSS is:")
	myInfo["STOKEN"] = input("Your STOKEN is:")
	jsonData = json.dumps(myInfo)
	configFile.write(jsonData)
	configFile.close()
	print("Set up complete.Data saved.")
else :
	myInfo = json.loads(configData)
		
Task =task.SignInTask(myInfo["BDUSS"],myInfo["STOKEN"]) #Initialize SignInTask instance

while True:
	print (
"""[1]Sign in one bar
[2]Sign in all
[3]Set up automatic sign in
[4]Disable automatic sign in"""
		)
	thisResult = int(input("What you want today:"))
	if thisResult == 1:
		kw = input("The kw is:")
		print(sign.SignIn(kw,myInfo["BDUSS"]))
	if thisResult == 2:
		print ("Signning...")
		Task.SignAll()
	if thisResult == 3:
		when = {}
		print ("When you want me to sign in everyday?/n")
		when["hour"] = int(input("The hour is:(0-23)"))
		while when["hour"]<0 or when["hour"]>23 :
			print("given value out of the range")
			when["hour"] = int(input("The hour is:(0-23)")) 
		
		when["minutes"] = int(input("The minutes is:(0-59)"))
		while when["minutes"]<0 or when["minutes"]>59 :
			print ("given value out of the range")
			when["minutes"] = int(input("The minutes is:(0-59)"))	
		Thread = task.AutoSignInThread(when,myInfo)
		Thread.start()
	if thisResult == 4 :
		print("stoped")#Task.SetAutoSignInStop()
