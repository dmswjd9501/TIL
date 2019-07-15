# # Startcamp Day1

## python 기초 문법

### 식별자

파이썬에서 식별자는 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름이다.

* 식별자의 이름은 영문알파벳, _, 숫자로 구성된다.

* 첫 글자에는 숫자 불가능

* 대소문자 구별한다

* ```python
  # 식별자 확인해보자
  import keyword
  print(keyword.kwlist)
  ```

### 변수

* 값 바꾸기

  ```python
  # 변수 x와 y의 값을 바꿔봅시다.
  x, y = 1004, 10002
  print(x, y)
  x, y = y, x
  print(x, y)
  ```

* 수치형(Numbers)

  파이썬 3.x 버전에서는 `long`타입이 없고 모두 `int`형으로 표기된다.

  8진수 : 0o 

  2진수 : 0b

  16진수 : 0x

* `float` (부동소수점, 실수)

  실수는 `float`로 표현된다.

  ```python
  b = 314e-2
  print(b) #3.14
  
  # 반올림을 해봅시다.
  round(3.5-3.12, 2) # 0.38
  
  # 두개의 값이 같은지 확인해봅시다.
  3.5-3.12 == 0.38 # False
  
  # 이외의 다양한 방법들이 있다.
  a = 3.5-3.12
  b = 0.38
  abs(a - b) <= 1e-10 # True
  
  # sys모듈 이용
  import sys
  abs(a - b) <= sys.float.info,epsilon # True
  
  # 파이썬 3.5부터 가능한 math 모듈
  import math
  math.isclose(a, b) # True
  
  if abs(a-b) <= 1e-10:
      print('같다')
      
  if(a == b):
      print('같다')
  else:
      print('다르다')
      
      
  # 복소수도 표현가능하다.
  a = 3 + 4j
  a.real # 3.0
  a.imag # 4.0
  a.conjugate() #
  ```

  

  

### 오버플로우(overflow)

- 데이터 타입 별로 사용할 수 있는 메모리의 크기가 제한되어 있다.
- 표현할 수 있는 수의 범위를 넘어가는 연산을 하게 되면, 기대했던 값이 출력되지 않는 현상, 즉 메모리가 차고 넘쳐 흐르는 현상

1. 저장

   ```python
   # 저장은 = 을 통해서 한다.
   dust = 64 # 숫자(integer)
   name = '홍길동' # 문자열(string)
   is_summer = True # 참/거짓, Boolean(True/False)
   ```

   ```python
   # 리스트 활용법
   my_list = [1,2,3,'정지수', '염겨레']
   print(my_list[0]) # => 1
   # 딕셔너리 활용법
   my_dictionary = {'정지수' : '남자', '염겨레' : '남자'}
   print(my_dictionary['정지수']) # => '남자'
   ```

   ```python
   # 리스트를 두 줄에 걸쳐서 만들어보자.
   lunch = [
       '짜장면', '짬뽕', '탕수육',
       '군만두', '물만두', '왕만두'
   ]
   # 딕셔너리를 두 줄에 걸쳐서 만들어보자
   my_dict = {
       'apple' : '사과',
       'banana' : '바나나',
       'candy' : '사탕'
   }
   ```

2. 조건

   ```python
   if dust > 150:
       print('매우나쁨')
   elif duct > 80:
       print('나쁨')
   else:
       print('보통')
   ```

3. 반복

   ```python
   lunch_box = ['짬뽕', '류산슬덮밥', '돈육제육..']
   # 정해진 리스트 반복
   for menu in lunch_box:
       # menu = lunch_box[0], ...., menu = lunch_box[2]
       print(menu)
   # n번 반복
   for menu in range(5):
       print('hello!!')
       
   ```

4. 내장함수

   > 내장함수는 별도로 import 구문이 필요없다.

   ```python
   print('hi')
   print(max([2, 4, 1])) # => 4
   print(min([1, 2, 5])) # => 1
   print(abs(-5)) # => 5
   print(len([1, 2, 3])) # => 3
   ```

5. 외장함수

   > 외장함수는 반드시  import가 필요하다.
   >
   > 다만, 파이썬을 설치하면 그냥 불러서 쓸 수 있다.

   ```python
   import random
   numbers = range(1, 46)
   lotto = random.sample(numbers, 6)
   print(sorted(lotto))
   ```

6. 패키지

   > 패키지는 반드시 설치를 필요로 한다.

   `pip install 패키지명` 으로 설치를 한다.

   ```bash
   $ pip install requests
   ```

   ```python
   import requests
   requests.get(url)
   ```





## 파이썬을 통한 크롤링

1. 필수 설치 패키지

   * `requests` :  파이썬으로 요청을 보내는 패키지

   * `bs4` : 문자열을 html 등으로 구조화(파싱)을 해주는 패키지

     ```bash
     $ pip install requests
     $ pip install bs4
     ```

2. 네이버에서 코스피지수 가져오기

   ```python
   # 0. 활용할 패키지를 불러온다.
   import requests
   from bs4 import BeautifulSoup
   # 1. url을 설정한다.
   url = 'https://finance.naver.com/sise/'
   # 2. 요청을 보내고, 그 결과의 내용을(text) response에 저장한다.
   response = requests.get(url).text
   # 3. html 문서로 변환한다.
   soup = BeautifulSoup(response, 'html.parser')
   # 4. 원하는 값을 선택자(selector)를 활용해서 가져온다.
   kospi = soup.select_one('#KOSPI_now').text
   print(kospi)
   
   ```

   