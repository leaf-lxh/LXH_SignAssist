#!python3
# coding:utf-8
#MySQLQuery.py
import pymysql

class MySQLOperate:
	def __init__(self, hostname, username, password):
		self.hostname = hostname
		self.username = username
		self.password = password
		self.databaseName = 'LXH_SignAssist'
		self.tablename = 'baidu_user_info'
	def Connect(self):
		try:
			database = pymysql.connect(self.hostname, self.username, self.password, self.databaseName)
			return database
		except :
			return None

	def QueryPrimarykey(self, tieba_username):
		database = self.Connect()
		
		cursor = database.cursor()
		
		statement = 'SELECT * FROM %s WHERE TIEBA_USERNAME = %s' %(self.tablename, tieba_username)
		try:
			cursor.execute(statement)
			result = cursor.fetchone()
			id = result[0]
		except:
			id = -1 #if there is no result,return -1
		database.close()	
		return id
	
	def QueryUserInfo(self,id):
		database = self.Connect()
		
		cursor = database.cursor()
		
		statement = 'SELECT * FROM %s WHERE id = %d' %(self.tablename, int(id))
		UserInfo = {}
		try:
			cursor.execute(statement)
			result = cursor.fetchone()
	
			UserInfo["ID"] = result[0]
			UserInfo["NAME"] = result[3]
			UserInfo["BDUSS"] = result[1]
			UserInfo["STOKEN"] = result[2]
			UserInfo["E_MAIL"] = result[4]
		except :
			UserInfo = None #if there is no result, return None
		database.close()
		return UserInfo

	def AddUserInfo(self,BDUSS,STOKEN,USERNAME,E_MAIL='NULL'):
		database = self.Connect()

		cursor = database.cursor()
	
		statment = """INSERT INTO %s (BDUSS,TIEBA_STOKEN,TIEBA_USERNAME,E_MAIL)
				VALUES(%s,%s,%s,%s)""" %(self.tablename,BDUSS,STOKEN,USERNAME,E_MAIL)
		try:
			cursor.execute(statement)
			db.commit()
		except:
			db.rollback()
		return

	def UpdateUserInfo(self,USERNAME,BDUSS=None,STOKEN=None,E_MAIL=None):
		database = self.Connect()
		
		cursor = database.cursor()
		statement = 'UPDATE %s SET'%(self.tablename)
		key = 0
		if BDUSS != None:
			statement+='BDUSS=%s'%(BDUSS)
			key+=1
		if STOKEN != None:
			statement+=',STOKEN=%s'%(STOKEN)
			key+=1
		if E_MAIL != None:
			statement+=',E_MAIL=%s'%(E_MAIL)
			key+=1
		if key == 0:
			return
		statement +='WHERE TIEBA_USERNAME=%s'%(USERNAME)
		try:
			cursor.execute(statement)
			db.commit()
		except:
			db.rollback()
		return
	def SetUserNULL(self,USERNAME):
		self.UpdateUserInfo('-','-',USERNAME,'-')
		return
