#!python3
# coding:utf-8

import os
import sys
import json
import time
import task
import MySQLQuery


configPath = "/etc/lxh"

def daemonInit():
	try:
		pid = os.fork()
		if pid > 0 :
			os._exit(0)
	except:
		task.WriteLog("fork failed,process exit...")

	os.setsid()
	os.chdir("/")
	os.umask(0)
	
	
	with open("/dev/null", 'rb', 0) as f:
		os.dup2(f.fileno(), sys.stdin.fileno())
	with open("/dev/null", 'ab', 0) as f:
		os.dup2(f.fileno(), sys.stdout.fileno())
	with open("/dev/null", 'ab', 0) as f:
		os.dup2(f.fileno(), sys.stderr.fileno())
	task.WriteLog("daemon process creation complete with pid %d"%(os.getpid()))
def main():
	
	task.WriteLog("process start")
	config = {
			"hour" : -1,
			"minute" :-1
	 	}
	try:
		with open(configPath+"/config.json",'r') as fileObject: #open() file and finally close()
			rawConfig = fileObject.read()    #read data
			if rawConfig != "":              #if file is not empty, transform data to dictionary
				config = json.loads(rawConfig) 
			else:
				raise RuntimeError("config file is empty")
				
	except : #if file is not exist or json data is not standard
		if os.path.isdir(configPath) == False:
			os.mkdir(configPath)	
		with open(configPath+"/config.json",'w') as fileObject:
			while config["hour"]<0 or config["hour"]>23:
				config["hour"] = int(input("Sign in hour is :(0-23)"))
			while config["minute"]<0 or config["minute"]>59:
				config["minute"] = int(input("Sign in minute is :(0-59)"))
			jsonData = json.dumps(config)
			fileObject.write(jsonData)

	task.WriteLog("config reading complete")
	user = input("MySQL username is :")
	password = input("password is:")
	test = MySQLQuery.MySQLOperate("localhost",user,password)
	if test.Connect() == None:
		print("Connect to MySQL failed.Try to check your username,password,your database name and table name")
		print("process exit")
		os._exit(0)
	print ("connect to database success,process is switching to background")
	daemonInit()
	
	Thread = task.AutoSignInThread(config,user,password)
	Thread.start()
	
if __name__ == "__main__":
	main()
