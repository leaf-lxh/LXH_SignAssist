import sign
import urllib.request

def GetILikeList(BDUSS,STOKEN):

	url = "http://tieba.baidu.com/f/like/mylike"
	Headers = {
			"Connection" : "keep-alive",
			"User-Agent" : "bdtb for Android 8.0",
			"Cookie" : "BDUSS=" + BDUSS +";STOKEN=" + STOKEN
		  }
	thisRequest = urllib.request.Request(url,headers=Headers)
	thisRequest = urllib.request.urlopen(thisRequest)
	response = str(thisRequest.read().decode("gbk"))
	print(response)	
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
