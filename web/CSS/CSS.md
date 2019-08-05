# CSS

### 1. position 속성으로 정렬하기

> 레이아웃을 배치하거나, 객체를 위치시킬 때 사용할 수 있는 속성



`1) position: static;`:  

- static은 초기값으로 위치를 지정하지 않을 때와 같다.

- 보통은 static을 사용할 일이 없지만, 앞에 설정된 position을 무시할 때 사용되기도 한다.

- top, bottom, left, right 속성값이 적용되지 않는다.



`2) position: relative;`: 

- relative는 위치 계산을 할 때 static의 원래 위치부터 계산한다.

- top, bottom, left, right의 위치를 설정할 수 있다.



`3) position: absolute;` : 

- absolute는 relative와 달리 문서의 원래 위치와 상관없이 위치를 지정할 수 있다.

- 하지만 **가장 가까운 상위요소**를 기준으로 (`단, static은 제외`) 위치가 결정된다.

- 상위요소가 없으면 위치는 html을 기준으로 설정된다.

- top, bottom, left, right의 위치를 설정할 수 있다.



`4) position: fixed;`: 

-  화면이 바뀌더라도 고정된 위치를 설정할 수 있다.(상위 요소에 영향을 받지 않음)
- top, bottom, left, right의 위치를 설정할 수 있다.

