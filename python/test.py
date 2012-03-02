import requests, datetime,xlrd

#define constants
PROXY_USERNAME = "INSERT"
PROXY_PASSWORD = "HERE"
#PROXY_LIST = {
#	'http':'http://'+PROXY_USERNAME+':%s@proxy.cpaaustralia.com.au:80' % PROXY_PASSWORD,
#	'https':'http://'+PROXY_USERNAME+':%s@proxy.cpaaustralia.com.au:80' % PROXY_PASSWORD,
#	'ftp':'http://'+PROXY_USERNAME+':%s@proxy.cpaaustralia.com.au:80' % PROXY_PASSWORD
#}
OATH_ENDPOINT = 'https://accounts.google.com/o/oauth2/auth?'
OATH_SCOPE = 'https://www.googleapis.com/auth/userinfo.email+https://www.googleapis.com/auth/analytics.readonly+https://www.googleapis.com/auth/userinfo.profile' #userinfo, email and analytics
OATH_REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
OATH_CLIENT_ID = '43620162052-fonhscvgrn3bs3jqn83krm3sqe9u0ti3.apps.googleusercontent.com'
OATH_CLIENT_SECRET = 'fLQvaXG5jHPkt4k910I8SYWk'
OATH_ACCESS_TOKEN = 'ya29.AHES6ZThRT57bjb_k4GGIi3C4TeW4z40Ie3haU3qLQKBFzg'
OATH_REFRESH_TOKEN = '1/IKxq0ly0m917kgbM3BIxN95y1l6z6Hki89EsL0-9gUU'

GA_URL = 'https://www.googleapis.com/analytics/v3/data/ga?'


def generate_request():
	return OATH_ENDPOINT+"client_id="+OATH_CLIENT_ID+"&scope="+OATH_SCOPE+"&redirect_uri="+OATH_REDIRECT_URI+"&response_type=code"

def get_tokens(auth_token):
	payload = {'code':auth_token,'client_id':OATH_CLIENT_ID,'client_secret':OATH_CLIENT_SECRET,'redirect_uri':OATH_REDIRECT_URI,'grant_type':'authorization_code'}
	connection = requests.post('https://accounts.google.com/o/oauth2/token',data=payload,proxies=PROXY_LIST)
	return connection.content

def refresh_token():
	payload = {'client_id':OATH_CLIENT_ID,'client_secret':OATH_CLIENT_SECRET,'refresh_token':OATH_REFRESH_TOKEN,'grant_type':'refresh_token'}
	connection = requests.post('https://accounts.google.com/o/oauth2/token',data=payload,proxies=PROXY_LIST)
	return connection.content

def get_ga_data(ga_id,start_date,end_date,dimensions,metrics,sort,max_results):
	header = {'Authorization:':'Bearer '+OATH_ACCESS_TOKEN}
	url = GA_URL+'ids='+ga_id+'&start_date='+start_date+'&end_date='+end_date+'&dimensions='+dimensions+'&metrics='+metrics+'&sort='+sort+'&max_results='+max_results
	connection = requests.get(url,headers=header,proxies=PROXY_LIST)
	return connection.content

#print refresh_token()
#print get_ga_data("ga:40923779",'2011-01-01','2011-01-30','ga:country','ga:visits','-ga:visits','50')
connection = requests.get('https://github.com',proxies=PROXY_LIST,verify=False,)
print connection.content
#OATH2 request: https://accounts.google.com/o/oauth2/auth?scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https://www.googleapis.com/auth/analytics.readonly+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile&redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=code&client_id=43620162052-fonhscvgrn3bs3jqn83krm3sqe9u0ti3.apps.googleusercontent.com

#OATH2 token POST: $ curl -x $tempproxy -d "code=4/UBVGn1tguzjlIrUDwcP-IotzzmDc&client_id=43620162052-fonhscvgrn3bs3jqn83krm3sqe9u0ti3.apps.googleusercontent.com&client_secret=fLQvaXG5jHPkt4k910I8SYWk&redirect_uri=urn:ietf:wg:oauth:2.0:oob&grant_type=authorization_code" https://accounts.google.com/o/oauth2/token

# OUTPUT
#   "access_token" : "ya29.AHES6ZThRT57bjb_k4GGIi3C4TeW4z40Ie3haU3qLQKBFzg",
#   "token_type" : "Bearer",
#   "expires_in" : 3600,
#   "id_token" : "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXVkIjoiNDM2MjAxNjIwNTItZm9uaHNjdmdybjNiczN
# qcW44M2tybTNzcWU5dTB0aTMuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJjaWQiOiI0MzYyMDE2MjA1Mi1mb25oc2N2Z3JuM2JzM2pxbjgza3JtM3N
# xZTl1MHRpMy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsImlkIjoiMTEwODc1NDM0NjE0MTczMzA0NTYyIiwiZW1haWwiOiJjcGFhbmFseXRpY3NAZ21
# haWwuY29tIiwidmVyaWZpZWRfZW1haWwiOiJ0cnVlIiwidG9rZW5faGFzaCI6IjVFcWd1aXBtLWV3cDFoMEk4TU9HYnciLCJpYXQiOjEzMjY4NjAxMjEsImV
# 4cCI6MTMyNjg2NDAyMX0.uQtDMdrywt3UuphM0BBtrUNwZMU-gMf0KFFo6doRGVBcDLTapn8PjMWtC5Uo93IjTrul95R6m5HNj3XWgyt6MeSRyG-OU9JShGx
# 1FOB2mH3d_oiXqJeqrj9OtTYvxF8KEM4QKfGZIRdUIn6Y7e0M8zQ8I-zt5BCjdnQn0sS3GyY",
#   "refresh_token" : "1/IKxq0ly0m917kgbM3BIxN95y1l6z6Hki89EsL0-9gUU"
