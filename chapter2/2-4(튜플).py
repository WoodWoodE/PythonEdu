# 튜플
# List와 거의 비슷한 개념, 자물쇠가 잠긴 서랍장이라고 생각하면 됨.

#List는 아래와 같이 값을 변경할 수 있었다.
# a = [1, 2, 3]
# a[0] = 5

# 튜플은 리스트와 거의 나머지 개념은 다 동일하나 변경이 불가능하다.
# b = (1, 2 , 3)
# b[0] = 5 => 에러 

#변경이 안되는 리스트라고 생각하면 됨.

# 변경이 안된다는 개념은 Mutable과 Imutable 자료형으로 두가지가 나뉘어 있다.
# Mutable은 변경이 가능한 자료형으로 리스트, 딕셔너리, 집합이 있다.
# Imutalbe은 변경이 불가능한 자료형으로 정수, 실수 ,문자열, 튜플이 있다.

# 리스트는 대괄호[]를 사용하고 튜플의 경우는 소괄호()를 사용한다.
t1 = ()
print(type(t1))

# 튜플에서 하나의 값이들어가면 ,를 넣어줘야만 한다.
t2 = (1,)
print(t2[0])

# 튜플을 만드는 방식은 다양한데 아래와 같다.
t3 = (1, 2, 3) 
print(t3)

t4 = 1, 2, 3 # 심지어 괄호 없이도 튜플을 만들 수 있다.
print(t4)

# 튜플 안에 튜플을 또 넣어줄 수 도 있다.
t5 = ('a', 'b', ('ab', 'cd'))

#==================================================

# 튜플의 값을 지우거나 변경하려고 하면 어떻게 되는가

# 튜플 값을 지우려고 할 때 
t6 = (1, 2, 'a','b')
# del t6[0] # 튜플은 아이템을 삭제하는게 불가능하다고 나옴.

#==================================================
# 튜플 다루기는 리스트와 거의 동일하기에 사실 거의 리스트를 복습한다는 개념으로 보면 됨.

#indexing
t7 = (1, 2, 'a','b')
print(t7[3])

#slicing
t8 = (1, 2, 'a','b')
print(t8[1:])

#튜플 더하기
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t3 = t1 + t2 # 새로운 튜플을 생성하는 것이기에 변형되는 것이 아님.
print(t3)

#sort, reverse, insert, del, remove 같은 변형하는 함수는 불가능함

#다른 것은 리스트와 완전 동일함