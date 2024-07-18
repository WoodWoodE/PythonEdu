#변수

# 변수는 상자와 같다.
# 값을 담는다고 했으나 실제로는 변수의 값을 담는게 아니라 메모리에 실제 값이 들어 있는데 이 값의 주소값을 담는다.

# 주소값을 확인하는 함수 - id()
a = 1 
b = 1
print(id(a)) # 이게 실제로 값이 들어 있는 주소이다.

# 객체를 깊은 복사하는법

# 리스트
print("{0:=^10}".format("리스트"))
a = [1,2,3,4,5]
b = a # => 얕은복사
c = a[:] # => 깊은복사 
print(a)
print(b)
print(c)
print(a is b)
print(a is c)

# 튜플 - 깊은복사 안되나봄..
print("{0:=^10}".format("튜플"))
a = (1,2,3,4,5)
b = a # => 얕은복사
c = a[:] # => 깊은복사 
print(a)
print(b)
print(c)
print(a is b)
print(a is c)

# 딕셔너리 - 뭔가 예시에 맞지 않음
print("{0:=^10}".format("딕셔너리"))
a = {1:10,2:20}
b = a # => 얕은복사
c = a.items() # => 깊은복사 
print(a)
print(b)
print(c)
print(a is b)
print(a is c)

# 집합
print("{0:=^10}".format("집합"))
a = set([1,2,3,4,5])
b = a # => 얕은복사
c = set(list(a)) # => 깊은복사 
print(a)
print(b)
print(c)
print(a is b)
print(a is c)

## COPY 모듈 이용
print("{0:=^10}".format("COPY 모듈 이용"))
from copy import copy
a = [1, 2, 3]
b = copy(a)
print(a is b)

## COPY 함수 사용
print("{0:=^10}".format("COPY 함수 이용"))
a = [1, 2, 3]
b = a.copy()
print(a is b ) 

##변수를 만드는 방법
# a = "python"
# b = "life"

a, b = ("python", "life") # => 이렇게도 할당이 가능하다.
print(a)
print(b)

# 튜플의 선언 종류는 세가지

(t) = "test", "test2"
print(t)

t = "test","test2"
print(t)

t = ("test","test2")
print(t)

#그래서 아래와 같이 변수를 넣어줘도 됨
(a, b) = "test", "test2"
print(a)
print(b)

a, b = "test", "test2"
print(a)
print(b)

a, b = ("test", "test2")
print(a)
print(b)

#리스트로 변수를 할당하는 것도 동일하게 가능하다
[a, b] = ["test", "test2"]
print(a)
print(b)

a, b = ["test", "test2"]
print(a)
print(b)

# 같은 값을 넣고 싶을때는 
a = "test"
b = "test"
#와 같이 넣고 싶다면, 아래와 같이 사용할 수 도 있다.
a = b = "test"
print(a)
print(b)

# 그리고 편리한 기능중 하나는 아래의 사례이다.
a = 3 
b = 5
#일때 a에는 5을 담고 b에는 3을 담고싶다(변수를 서로 교체하고 싶다)면 다른 언어의 경우는 임시 변수를 생성해서 넣어 줬어야만 했다
# temp = a # 잠시 a를 담고
# a = b    # a에 b를 담고
# b = temp # b에 잠깐 담아 뒀던 a의 값을 넣어주면 a와 b의 값이 교체된다

#그런데 파이썬의 경우는 
a, b = b, a #와 같이 사용할 수 있다.
print(a)
print(b)

