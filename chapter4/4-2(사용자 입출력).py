# 사용자 입출력

# 사용자 입력 활용하기

# input 사용하기
# a = input()
# print(a)

# input함수의 내부에 문자열을 입력하면 입력 전에 해당 문자열을 출력시킨다
# a = input("문자열을 입력하세요 : ")
# print(a)

# input 으로 입력되는 모든값은 문자열이기에 숫자를 입력하더라도 문자열임을 알고 있어야한다.

## print문에 대해서 

# 큰따옴표로 둘러싸인 문자열은 + 연산과 동일하다
print("Head" "Body" "Tail")
print("Head" + "Body" + "Tail")

# 문자열 띄어쓰기는 쉼표를 사용한다
print("Head", "Body", "Tail")

# 한 줄에 결괏값 출력하기
for i in range(1, 11):
    print(i, end=" ")