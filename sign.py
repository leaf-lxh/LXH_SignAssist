import urllib.request
import urllib.parse
import hashlib

def GetFID(kw):
	
	url="http://tieba.baidu.com/f/commit/share/fnameShareApi?ie=utf-8&fname=" + urllib.parse.quote(str(kw))
	thisRequest = urllib.request.urlopen(url)
	Response = thisRequest.read()
	PositionA = str(Response).find(r'"fid":')
	PositionA += len(r'"fid":')
	PositionB = str(Response).find(',' , PositionA)

	return str(Response)[PositionA:PositionB]

def GetTBS(kw , BDUSS):

	url="http://tieba.baidu.com/mo/m?kw=" + urllib.parse.quote(str(kw))
	Headers = {	
			"User-Agent" : "bdtb for Android 8.0",
			"Cookie" : "BDUSS=" + BDUSS
		  }
	thisRequest = urllib.request.Request(url,headers=Headers)
	thisRequest = urllib.request.urlopen(thisRequest)
	response = str(thisRequest.read())
	PositionA = response.find(r'name="tbs" value="')
	PositionA += len(r'name="tbs" value="')
	PositionB = response.find('\"' , PositionA)
	return response[PositionA:PositionB]

def SignIn(kw , BDUSS):
		
	url = "http://c.tieba.baidu.com/c/c/forum/sign"
	#create arguments for the sign in post
	fid = GetFID(kw)
	tbs = GetTBS(kw , BDUSS)
	parameter="BDUSS=" + BDUSS + "&fid=" + fid + "&kw=" + kw + "&tbs=" +tbs + "&sign="
	sign = "BDUSS=" + BDUSS + "fid=" + fid + "kw=" + kw + "tbs=" +tbs + "tiebaclient!!!"
	
	signMD5 = hashlib.md5()
	signMD5.update(sign.encode("utf8"))
	sign = str(signMD5.hexdigest()).upper()
	parameter += sign
	parameter = parameter.replace('+',"%2B") #urlencode problem, urlencode will convert '+' to ' '
	print(parameter)
	
	Headers = {
			"User-Agent" : "bdtb for Android 8.0",
			"Content-Type" : "application/x-www-form-urlencoded"	
		  }

	thisRequest = urllib.request.Request(url,headers=Headers,data=bytes(parameter,"utf8"))
	thisRequest = urllib.request.urlopen(thisRequest)	
	response = thisRequest.read().decode("unicode-escape")  #This is the first time I saw such a type "unicode-escape".
	return response
