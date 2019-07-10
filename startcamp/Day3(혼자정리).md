# HTML

## 구조 

* `HTML` : 전체적인 구조

  * ```html
    <!DOCTYPE html>
    <html lang = 'ko'>
        
        <head>
            <meta charset = "utf-8">
            <title> 인터넷 창 이름</title>
            <style>
               /* 글자색 정해주는 부분 */
            </style>
        </head>
        <body>
            /* 내용을 정해주는 부분 */
          
            
        </body>
    </html>
    ```

  *   h1(heading) : 가장 큰 제목
      h2(heading) : 소제목
      h6(heading) : 가장 작은 제목
      p : 내용

    <br>`CSS` : 디자인 

  * `style`

    - 글자색 바꾸기

    ```html
    h1{
    	color: red;
    }
    ```

    - 글씨 정렬하기

    ```html
    h1{
    	text-align: center;
    	# 가운데 정렬 : center
    	# 왼/오 정렬 : left/right
    }
    ```

  * 우선순위 정렬 : `id` > `class` > `태그`

    `id`는 문서에서 하나만 존재할 수 있다.

    `class`는 문서에서 여러개 존재할 수 있다. 

    `태그`는 그냥 기본이다.

    > 'index.html' 예제를 보면,  `h2`인 경우 `id="pink"` `class="red"` 둘 중에 어떤 색깔을 따라갈 것인가?

    -> 우선순위로 인해서 `id="pink"`이므로 핑크색으로 설정된다.

    
    
    
    
    
    
    