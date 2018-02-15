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
		

while True:
	print (
"""[1]Sign in one bar
[2]Sign all
[3]Set up automatic signing"""
		)
	thisResult = int(input("What you want today:"))
	if thisResult == 1:
		kw = input("The kw is:")
		print(sign.SignIn(kw,myInfo["BDUSS"]))
	if thisResult == 2:
		print ("Signning...")
		task.SignAll(myInfo["BDUSS"],myInfo["STOKEN"])
