#task.py
#!python3
# coding: utf-8
import sign
import MySQLQuery
import urllib.request
import time
import threading

logPath = "/var/log/lxh"

def WriteLog(string):
	try:
		with open(logPath+"/output.log","a") as fileObject:
			fileObject.write(time.asctime(time.localtime(time.time())) + "  ")
			fileObject.write(string)
			fileObject.write("\n")
	except:
		if os.path.isdir(logPath) == False:
			os.mkdir(logPath)
		with open(logPath+"/output.log","w") as fileObject:
			pass
		WriteLog(string)

class SignInTask:

	def __init__(self,BDUSS,STOKEN):
		self.BDUSS = BDUSS
		self.STOKEN = STOKEN

	def GetILikeList(self):
	
		url = "http://tieba.baidu.com/f/like/mylike"
		Headers = {
				"Connection" : "keep-alive",
				"User-Agent" : "bdtb for Android 8.0",
				"Cookie" : "BDUSS=" + self.BDUSS +";STOKEN=" + self.STOKEN
			  }
		thisRequest = urllib.request.Request(url,headers=Headers)
		thisRequest = urllib.request.urlopen(thisRequest)
		response = str(thisRequest.read().decode("gbk"))	
		#check the web source ,see if there has data that we need
		if response.find(r'" title="') != -1 :
			isStill = True
		else :
			isStill = False
			
		ILikeList = {}
		pB=0
		while isStill :
			pA = response.find(r'" title="',pB)	
			pA += len(r'" title="')
			pB = response.find('\"',pA)
			kw = response[pA:pB]
			
			pA = response.find(r'" title="',pB)
			pA += len(r'" title="')
			pB = response.find('\"',pA)
			lev = response[pA:pB]
			
			ILikeList[kw] = lev
	
			if response.find(r'" title="',pB) == -1 :
				break	
		return ILikeList
	
	
	def SignAll(self):
		
		ILikeList = self.GetILikeList()
		for kw,lev in ILikeList.items():
			print (kw)
			WriteLog(sign.SignIn(kw,self.BDUSS))
			
			time.sleep(10)#The interval of each sign in is 10 seconds.

class AutoSignInThread(threading.Thread) :# Inherit form threading.Thread 
	
	def __init__(self,when,MySQLUserName,MySQLpassword):
		self.when = when
		self.user = MySQLUserName
		self.passwd = MySQLpassword
		self.isEnabled = False
		threading.Thread.__init__(self)
		
	def run(self):
		
		if self.isEnabled == True:
			return #make sure only create one watching thread
		self.isEnabled = True
		self.todayDay = (time.localtime(time.time()))[2] #Get the day of this thread created
		self.lastSignInDay = self.todayDay - 1
		while self.isEnabled == True:
			
			self.todayDay = (time.localtime(time.time()))[2]
			if self.lastSignInDay != self.todayDay :
				
				if self.when["hour"] == (time.localtime(time.time()))[3] :	
					if self.when["minute"] == (time.localtime(time.time()))[4]:
						sql = MySQLQuery.MySQLOperate("localhost",self.user,self.passwd)
						id = 1
						while True:
							UserInfo=sql.QueryUserInfo(id)
							print(UserInfo)
							if UserInfo == None:
								break
							sign = SignInTask(UserInfo["BDUSS"],UserInfo["STOKEN"])
							sign.SignAll()
							id+=1
							WriteLog("%s has sign in"%(UserInfo["NAME"]))
						self.lastSignInDay = self.todayDay
			WriteLog("Thread is running....")
			time.sleep(30)
