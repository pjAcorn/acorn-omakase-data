import requests
import pprint
import json
from bs4 import BeautifulSoup
# import pandas as pd

# 인증키
encodingKey = "e%2BhnMTtUR6KCEeT0JaUw91rq9kQKnCDlWy5kQug3YNpYGx0gHDpQN6dMtNV7IfFt9irWjAbV60gDoq827vCPgQ%3D%3D"
decodingKey = "e+hnMTtUR6KCEeT0JaUw91rq9kQKnCDlWy5kQug3YNpYGx0gHDpQN6dMtNV7IfFt9irWjAbV60gDoq827vCPgQ=="

# URL
url = "http://api.odcloud.kr/api/15083033/v1/uddi:bb89aa82-09a4-4d4d-91d9-9d6681bb09a7"
params = {'serviceKey': decodingKey, 'pageNo': 1, 'numOfRows': 10}

response = requests.get(url, params=params)
# contents = response.text

# 깔끔한 출력
# pp = pprint.PrettyPrinter(indent=4)
# print(pp.pprint(contents)) 

# 예쁘게 출력하기

soup = BeautifulSoup(response.text, "html.parser")
# print(soup)

strSoup = str(soup)
strSoup = strSoup[27:]
splitList = strSoup.split("}")

for s in splitList:
    print(s.lstrip("{"))

# list = []
# for item in soup.find_all("item"):
#     overcrowding = item.find("과밀지수").text
#     name = item.find("상권명칭").text
#     list.append([overcrowding, name])


# print(list)
# city_df = pd.DataFrame(list, columns= ["overcrowding", "name"])
# city_df.head()