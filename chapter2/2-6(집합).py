#집합
# 교집합, 합집합, 차집합 같은걸 자료형으로 제공함

#집합에 관련된 것을 쉽게 처리하기 위해서 개발한 것 

#집합은 set이라고 부르고 키워드로 사용할 수 있다.

#집합 자료형은 List로도 String으로도 만들 수 가 있다.

s1 = set([1, 2, 3]) # => str(123)과 비슷한 사용법임
print(s1)
print(type(s1))

#set은 중괄호{}에 딕셔너리처럼 key, value쌍이 아닌 그냥 배열처럼 값이 들어 있다.

# 그냥 기본적으로 만드는 방법은 아래와 같다.
s1 = {1, 2, 3}
print(type(s1))

# String도 집합으로 변경이 가능하다
s1 = set("Hello")
print(type(s1))
#그런데 변경된 결과물은 집합의 형태를 가지는데 중복된 값은 제거되고 순서도 순차적이지 않다.
print(s1) # 실행할때마다 결과물이 달라짐(순서)

#이건 집합의 특성 때문이다.
# 집합은 순서라는 개념이 없고 원소가 각각 고유하기 때문에 값이 순차적이지 않고 중복되지 않는다.
# 순서라는 개념이 없기 때문에 index로 접근한다는 것 자체도 불가능하다.

# 만약 집합을 만들었는데 궂이 값을 갖고 오고 싶다면 List로 감싸주고 값을 가져오면 된다.
s1 = set([1, 2, 3])
l1 = list(s1)
print(l1[0])


# 그럼 집합을 왜쓰는가? 
# 교집합, 합집합, 차집합을 구하는 함수등 자료형에서 제공해주는 기능때문에 사용한다.

# 교집합 구하기
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1&s2) # => 교집합 구하는 방법

# 교집합 함수로 구하기 - Set.intersection(비교하려는 Set)
print(s1.intersection(s2))

#####

# 합집합 구하기
print(s1 | s2) # => 교집합 구하는 방법

# 합집합 함수로 구하기 - Set.union(합치려는 Set)
print(s1.union(s2))

#####

# 차집합 구하기
print(s1 - s2)

# 차집합 함수로 구하기 - Set.difference(합치려는 Set)
print(s1.difference(s2))

#####
#집합에 하나의 값 추가하기 - add()
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

#####
#집합에 여러개 값 추가하기 - update()
s1 = set([1, 2, 3])
s1.update([4,5,6]) # 다수의 값을 추가할 때에는 [] 배열의 형태로 저장해야함
s1.update([4, 4, 5, 6]) # 중복되는 값이 있다면 중복을 제거한 채로 삽입된다.
s1.update({1 : "1"}) # => 추가안됨, 오류는 안남
# s1.add([1,2]) # => add의 경우 다중으로 삽입할 경우 오류남
# s1.add(7,8) # => add의 경우 다중으로 삽입할 경우 오류남
print(s1)

#####
#집합에 특정 값 제거하기 - remove(value)
s1 = set([1, 2, 3])
s1.remove(2)
# s1.remove([2,3]) # => 다수의 값을 제거하는 것 도 에러를 벹음
# s1.remove(4) # => 없는 값을 넣으면 에러를 벹음
print(s1)

### 언제 자주 활용하는가?
# 리스트가 있는데 중복되는 내용이 많다
l1 = [1,2,2,3,3,3,3,4,4,4,4,4,4]
# 그러면 중복을 제거해서 다시 쓰고 싶은 경우
s1 = set(l1) # => 중복제거
print(s1)
l1 = list(s1) # => list로 변경
print(l1)

# 이걸 축약해선 
l1 = [1,2,2,3,3,3,3,4,4,4,4,4,4]
l1 = list(set(l1))
print(l1)
# 보통 집합은 랜덤하게 되는데 set으로 감쌌다가 list로 바꾸면 순서를 어느정도를 유지하긴 한다.
