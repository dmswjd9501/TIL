import requests
import csv
import pprint


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


information={}
director_info = response['movieInfoResult']['movieInfo']