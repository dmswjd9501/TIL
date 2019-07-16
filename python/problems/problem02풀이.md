```python
# 1. 모든 코인 상승장? 하락장?
for key in data.keys():
    if key == 'date':
        continue
    change = float(data[key]['max_price']) - float(data[key]['min_price'])
    result = change + float(data[key]['opening_price'])
    if result > float(data[key]['max_price']):
        print('상승장')
    else:
        print('하락장')
```

```python
# 2. 평균점수 구하기
hap = 0
for value in student.values():
    hap += value
print(f'평균 점수는 {hap / len(value)}입니다.')
```

```python
# 3. 혈액형 몇 명인지 구하기
result_A = 0
result_B = 0
result_AB = 0
result_O = 0

for i in blood:
	if i == 'A':
		result_A += 1
	elif i == 'B':
		result_B += 1
	elif i == 'AB':
		result_AB += 1
	else:
		result_O += 1

print(f'A형은 {result_A}명, B형은 {result_B}명, AB형은 {result_AB}명, O형은 {result_O}명입니다.')
```

```python
# 4. 영화관람객 미만인 영화 출력
for key, value in movies.items():
    if value <= 80 * 172212
    	print(key)
```

