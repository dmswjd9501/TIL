import requests

key = '4541b77c39ed819f55b6d3b2da045cb6'
targetDt = '20190713' #yyyymmdd
api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}'
print(api_url)
response = requests.get(api_url).json()
print(response)