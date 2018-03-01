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
		database = pymysql.connect(self.hostname, self.username, self.password, self.databaseName)
		return database
	
	def QueryPrimarykey(self, tieba_username):
		database = self.Connect()
		
		cursor = database.cursor()
		
		statement = 'SELECT * FROM %s WHERE TIEBA_USER_NAME = %s' %(self.tablename, tieba_username)
		try:
			cursor.excute(statement)
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
			cursor.excute(statement)
			result = cursor.fetchone()
	
			UserInfo["ID"] = result[0]
			UserInfo["NAME"] = result[3]
			UserInfo["BDUSS"] = result[1]
			UserInfo["STOKEN"] = result[2]
		except:
			UserInfo = None #if there is no result, return None
		database.close()
		return UserInfo

	def AddUserInfo(self,BDUSS,STOKEN,USERNAME,E_MAIL='NULL'):
		database = self.Connect()

		cursor = database.cursor()
	
		statment = """INSERT INTO %s (BDUSS,TIEBA_STOKEN,TIEBA_USERNAME,DAY_LASTSIGNIN,E_MAIL)
				VALUES(%s,%s,%s,0,%s)""" %(self.tablename,BDUSS,STOKEN,USERNAME,E_MAIL)
		try:
			cursor.excute(statement)
			db.commit()
		except:
			db.rollback()
		return
