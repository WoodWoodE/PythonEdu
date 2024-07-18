# 불 자료형
# 참(True) & 거짓(False)
# 조지 불 이라는 사람의 이름에서 따온것임

# 조건문에서 사용됨

a = True # => String과 다름
print(a)
print(type(a))

#주의할 점은 첫글자는 무조건 대문자로 사용해야한다.

# ==를 사용해서 bool자료형 만들기
a = 1 == 1
print(a)
a = 1 != 1
print(a)

# 자료형의 참과 거짓
#자료형에도 참과 거짓을 따지는 값들이 따로 있다.
# 문자열, 튜플, 딕셔너리 => 값이 있다면 True / 값이 없으면 False
# 숫자형 자료형은 0 => 거짓 / 0을 제외한 모든 수는 거짓
# None => 거짓을 의미함


# while 문에서의 불 타입의 사용
a = [1, 2, 3, 4]
while a :
    print(a)
    a.pop()
# => a의 값이 하나씩 제거되다 빈 리스트가 되면 a 가 거짓이 되면서 while문을 벗어난다.

# 조건문(if-else)에서 불 타입의 사용
if [] :
    print("True")
else:
    print("False")
##
if [1,2] :
    print("True")
else:
    print("False")
    
# 해당 값이 참인지 거짓인지를 직접 확인하기 위해서는 bool으로 형변환하면 확인이 가능하다.
a = bool([1,2,3])
print(a)

a = bool([])
print(a)

a = bool({1:12,2:13,3:16})
print(a)

a = bool({})
print(a)

a = bool((1,2))
print(a)

a = bool(())
print(a)

a = bool(123124)
print(a)

a = bool(0)
print(a)


