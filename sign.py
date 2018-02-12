import urllib.request
def GetFID(kw):

	url="http://tieba.baidu.com/f/commit/share/fnameShareApi?ie=utf-8&fname=" + str(kw)
	thisRequest = urllib.request.urlopen(url)
	Response = thisRequest.read()
	PositionA = str(Response).find(r'"fid":')
	PositionA += len(r'"fid":')
	PositionB = str(Response).find(',' , PositionA)

	return str(Response)[PositionA:PositionB]

def SignIn(kw, BDUSS):
	fid = GetFID(kw)	
