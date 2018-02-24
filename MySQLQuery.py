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
	
	def QueryPrimarykey(self, tieba_username)
		database = self.Connect()
		
		cursor = database.cursor()
		
		statement = 'SELECT * FROM %s WHERE TIEBA_USER_NAME = %s' %(self.tablename, tieba_username)
		try:
			cursor.excute(statement)
			result = cursor.fetchone()
			id = result[0]
		except:
			id = -1
		database.close()	
		return id
	
	def QueryUserinfo(self,id):
		database = self.Connect()
		
		cursor = database.cursor()
		
		statement = 'SELECT * FROM %s WHERE id = %d' %(self.tablename, id)
		UserInfo = {}
		try:
			cursor.excute(statement)
			result = cursor.fetchone()
	
			UserInfo["ID"] = result[0]
			UserInfo["NAME"] = result[3]
			UserInfo["BDUSS"] = result[1]
			UserInfo["STOKEN"] = result[2]
		except:
			UserInfo = None
		return UserInfo
