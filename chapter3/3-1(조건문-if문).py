#조건문(if문)
# 돈이 있으면 택시를 타고, 돈이 없으면 걸어간다
# 와 같이 어떤 조건에 따라 행위의 변동을 줘야할 때 사용한다.

money = True # True : 돈이 있다. / False : 돈이 없다.

if money : 
    print("택시를 탄다.")
else:
    print("걸어 간다.")
    
# 이를 조건문이라고 부른다.

# 조건문의 구조는 그냥 비슷함

# * 다른점
# 들여쓰기가 강제됨, 들여쓰기 레벨도 맞춰져야함, : 은 꼭 있어야만 한다.

# 비교연산자 - 똑같음

# and , or, not
# x or y - 둘중 하나 (|의 기능과 동일)
# x and y - 둘 다 (&의 기능과 동일)
# not x - x가 거짓이면 참이됨(!의 기능과 동일)


# in, not in -리스트, 튜플, 문자열에서 해당
# x in 리스트 - x not in 리스트
# x in 튜플 -  x not in 튜플
# x in 문자열 - x not in 문자열

#리스트에서 사용법 
print(1 in [1, 2, 3 ])

#튜플에서 사용법 
print(1 in (1, 2 , 3))

#문자열에서 사용법
print('a' in "apple")

# not은 그냥 반대로 사용됨 

#이제 이걸 응용해서 만약에 주머니에 돈이 있으면 택시를 타고 없으면 걸어가라 라고 만들어보자
pocket = ["paper", "cellphone", "money"]

if "money" in pocket:
    print("택시를 탄다.")
else:
    print("걸어간다.")

# 조건문에서 아무 일도 없게 설정하고 싶다면, pass 를 쓰면 된다
# 그냥 비우면 되는거 아니냐? 파이썬에선 비워두면 오류남

if "money" in pocket:
    pass
else:
    print("걸어간다.")

# 다양한 조건을 판단하는 elif
# 조건은 보통 여러개가 있는 경우가 많기 때문에 자주 사용됨

# 돈도 없고 카드도 없다면 걸어가라
pocket = ["paper", "cellphone", "money"]
# pocket.remove("money")
# pocket.append("card")

if "money" in pocket:
    print("현금으로 택시를 타라")
elif "card" in pocket:
    print("카드로 택시를 타라")
else:
    print("걸어가라.")

# if문을 한줄로 작성하기
if 'money' in pocket: pass
else: print("걸어가라")

# 가독성이 떨어져서 두줄로 쓰는게 일반적이다.

# 조건부 표현식 - 줄여쓰는 방법중 하나임. 자바에서는 3항 연산자를 말하는 것으로 보임 - 많이는 안쓰나봄..

# 참일때 실행할 코드 if 조건문 else 거짓일때 실행할 코드

score = 57

print("합격입니다.") if score > 60 else print("불합격입니다.")

#자료형의 참과 거짓
a = 'python'

if a : 
    print("참입니다.")

a = ''

if a : 
    print("참입니다.")
else:
    print("거짓입니다.")
