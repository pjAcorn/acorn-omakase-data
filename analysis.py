import requests
import pprint
import json

# 인증키
encodingKey = "e%2BhnMTtUR6KCEeT0JaUw91rq9kQKnCDlWy5kQug3YNpYGx0gHDpQN6dMtNV7IfFt9irWjAbV60gDoq827vCPgQ%3D%3D"
decodingKey = "e+hnMTtUR6KCEeT0JaUw91rq9kQKnCDlWy5kQug3YNpYGx0gHDpQN6dMtNV7IfFt9irWjAbV60gDoq827vCPgQ=="

# URL
url = "http://api.odcloud.kr/api/15083033/v1/uddi:5926b965-2a6b-498f-9757-8eb34949e0fc"
params = {'serviceKey': decodingKey, 'pageNo': 1, 'numOfRows': 10}

response = requests.get(url, params=params)
contents = response.text

pp = pprint.PrettyPrinter(indent=4)
print(pp.pprint(contents))

# 미완성, NONE으로 불러오기되는 오류 해결할 것