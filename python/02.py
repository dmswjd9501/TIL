import requests
import csv
import pprint
detail_info={}

f = open('01.csv', 'r', encoding='utf-8')
rdr = csv.DictReader(f)
for line in rdr:
    print(line)



    key = '4541b77c39ed819f55b6d3b2da045cb6'
    movieCd = line['영화코드']
    api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={movieCd}'
    print(api_url)
    response = requests.get(api_url).json()
    # pprint.pprint(response)

    info={}
    movie_info = response['movieInfoResult']['movieInfo']

    movieCd = movie_info.get('movieCd')  # 큰 딕셔너리에서 가지고 올 때! 
    movieNm = movie_info.get('movieNm')
    movieNmEn = movie_info.get('movieNmEn')
    movieNmOg = movie_info.get('movieNmOg')
    showTm = movie_info.get('showTm')
    openDt =  movie_info.get('openDt')
    watchGradeNm = movie_info.get('audits')[0]['watchGradeNm'] if movie_info.get('audits') else None
    genreNm = movie_info.get('genres')[0]['genreNm'] if movie_info.get('genres') else None
    peopleNm = movie_info.get('directors')[0]['peopleNm'] if movie_info.get('directors') else None


    info['영화대표코드'] = movieCd
    info['영화명(국문)'] = movieNm
    info['영화명(영문)'] = movieNmEn
    info['영화명(원문)'] = movieNmOg
    info['상영시간']= showTm
    info['개봉연도'] = openDt
    info['관람등급'] = watchGradeNm
    info['장르'] = genreNm
    info['감독명'] = peopleNm


    detail_info[movieCd] = info

    print(detail_info)

    import csv
    with open('02.csv', 'w', encoding='utf-8') as f:
        fieldnames = ['영화대표코드', '영화명(국문)', '영화명(영문)','영화명(원문)', '상영시간', '개봉연도', '관람등급', '장르', '감독명'] # 여기만 변경
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()
        # csv_writer.writerow(detail_info)
        for item in detail_info.values(): # 딕셔너리 만든 것 반복
            print(item)
            csv_writer.writerow(item)