# 리스트 자료형
# 리스트란 해야할 일 같은 개념이다.
# 변수를 여러개 넣어둔 개념이다.

# 리스트의 생성법
odd = [1, 3, 5, 7, 9]
print(type(odd))

# 다른 언어와 다른점은 타임을 다중으로 넣을 수 있는 것이다. 속도면에 비효율
e = [1, 2, "Life", "is"]

#그리고 List안에 List를 넣을 수 있다.
e = [1, 2, ["Life", "is"]]

#리스트의 인덱싱 - string이랑 거의 동일함
a = [1, 2, 3]
print(a[1])

print(a[1] + a[2]) # String일때는 23이 나오는데 숫자형이기에 5가 나옴

#-를 넣으면 거꾸로 불러옴
print(a[-1])
print(a[-1] + a[-2])

# 만약 리스트 내부에 리스트가 또 존재할 경우
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[3])
print(a[3][1]) # 리스트 내부의 리스트의 인덱싱

# 이런경우가 매우 많다고함

#동일하게 -로도 가능하다.
print(a[-1][-1]) # 리스트 내부의 리스트의 인덱싱
print(a[-1][2]) # 리스트 내부의 리스트의 인덱싱

# 내부 리스트가 아닌 경우는 문자열일때를 제외하곤 에러를 출력한다.
a = [1, 'hello', 3, ['a', 'b', 'c']]
# print(a[2][2]); - 에러 

# 문자열은 문자 열이기 때문에 출력이 된다.
print(a[1][1]);

# 슬라이싱 - 문자열과 거의 동일함..
a = [1, 2, 3, 4, 5]
print(a[0:2]) # 0번째 인덱스부터 2번째 인덱스 미만까지를 보여줘라 
print(a[::2]) # 0번째 인덱스부터 끝까지 두칸씩 보여줘라 


# 중첩된 리스트에서 슬라이싱하기 
a = [1, 2, 3, ["a", "b", "c"], 4, 5]
print(a[2:5])
print(a[3][:1])
print(a[3][::2])

# 리스트 연산하기

# - 리스트 더하기
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b) # 두개의 리스트를 합치는 기능을 함

# - 리스트 곱하기
print(a * 2)
#print(a * '3') 숫자를 제외하고는 연산할 수 없다.

