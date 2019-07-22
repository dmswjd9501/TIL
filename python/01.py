import requests
import pprint
from datetime import datetime, timedelta

key = '4541b77c39ed819f55b6d3b2da045cb6'
targetDt = '20190713' #yyyymmdd
weekGb = '0'

movies={}
    
    
for i in range(50):
    api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb={weekGb}'
    print(api_url)
    targetDt_convert = datetime.strptime(targetDt, "%Y%m%d").date()
    week_ago = targetDt_convert + timedelta(days=-7)
    targetDt = week_ago.strftime("%Y%m%d")
    response = requests.get(api_url).json()
    pprint.pprint(response)
    
    for movie in response['boxOfficeResult']['weeklyBoxOfficeList']:

        if movie['movieCd'] not in movies:
            code_dict={}
            code = movie['movieCd']
            name = movie['movieNm']
            audi = movie['audiAcc']
            
            code_dict['이름'] = name
            code_dict['영화코드'] = code
            code_dict['누적관객수'] = audi
            movies[movie['movieCd']] = code_dict

print(movies)
import csv
with open('01.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['이름', '영화코드', '누적관객수'] # 여기만 변경
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in movies.values(): # 딕셔너리 만든 것 반복
        csv_writer.writerow(item)