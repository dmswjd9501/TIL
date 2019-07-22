import requests
import pprint
import csv
from datetime import datetime, timedelta

people_result={}
f = open('02.csv', 'r', encoding='utf-8')
rdr = csv.DictReader(f)
for line in rdr:
    print(line)


    key = '4541b77c39ed819f55b6d3b2da045cb6'
    peopleNm = line['감독명']
    api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={key}&peopleNm={peopleNm}'
    print(api_url)
    response = requests.get(api_url).json()
    pprint.pprint(response)


    people_info={}
    people_info = response['peopleListResult']['peopleList']
    if '감독' == people_info[0]['repRoleNm'] and peopleNm == people_info[0]['peopleNm']:
        people_result[peopleNm] = {
            '영화인명': people_info[0]['peopleNm'] if people_info[0] else None,
            '영화인 코드': people_info[0]['peopleCd'] if people_info[0] else None,
            '분야': people_info[0]['repRoleNm'] if people_info[0] else None,
            '필모리스트': people_info[0]['filmoNames'] if people_info[0] else None,
        }
    # pprint.pprint(people_result)



    
    with open('03.csv', 'w', encoding='utf-8') as f:
        fieldnames = ['영화인명', '영화인 코드', '분야', '필모리스트'] # 여기만 변경
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()
        # csv_writer.writerow(detail_info)
        for item in people_result.values(): # 딕셔너리 만든 것 반복
            print(item)
            csv_writer.writerow(item)