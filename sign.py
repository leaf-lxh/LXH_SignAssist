import urllib.request

def GetFID(kw):

	url="http://tieba.baidu.com/f/commit/share/fnameShareApi?ie=utf-8&fname=" + str(kw)
	thisRequest = urllib.request.urlopen(url)
	Response = thisRequest.read()
	PositionA = str(Response).find(r'"fid":')
	PositionA += len(r'"fid":')
	PositionB = str(Response).find(',' , PositionA)

	return str(Response)[PositionA:PositionB]

def GetTBS(kw,BDUSS):

	url="http://tieba.baidu.com/mo/m?kw=" + str(kw)
	Headers = {	
			"User-Agent" : "bdtb for Android 9.0",
			"Cookie" : "BDUSS=" + BDUSS
		  }
	thisRequest = urllib.request.Request(url,headers=Headers)
	thisRequest = urllib.request.urlopen(thisRequest)
	response = str(thisRequest.read())
	PositionA = response.find(r'name="tbs" value="')
	PositionA += len(r'name="tbs" value="')
	PositionB = response.find('\"' , PositionA)
	
	return response[PositionA:PositionB]

def SignIn(kw, BDUSS):
	fid = GetFID(kw)
		
