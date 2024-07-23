# for문

# for문의 기본 구조 

# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할 문장1
#     수행할 문장2
#     ...

# 전형적인 for 문 
count = ["one","two","three","four"]

for cnt in count:
    print("현재 루프도는 수는 영문으로 %s입니다" %cnt)
    
# 다양한 for문의 사용
a = [(1,2),(3,4),(5,6)]

for (first, last) in a:
    print(first + last)
    
# a 리스트의 요소값이 튜플이기에 각각 요소가 자동으로 first와 last에 대입된다
# 그러면 리스트는 ?

a = [[1,2,3],[4,5,6],[7,8,9]]

for [fst,snd,trd] in a:
    print(fst)
    print(snd)
    print(trd)
    print(type(fst))
    print(type(snd))
    print(type(trd))
    
for (fst,snd,trd) in a:
    print(fst)
    print(snd)
    print(trd)
    print(type(fst))
    print(type(snd))
    print(type(trd))
    
for (fst) in a:
    print(fst)
    print(type(fst))
    
# for 변수 in에 변수는 어떤 형태든 상관없이 풀어지는듯 보임
# ()로 묶던 []로 묶던 상관없이 그 내부가 풀린 형태로 반환됨 => 이건 아예 문법에서 영향을 주지 않는듯 보임, 중괄호만 아니면 되는듯

# 자주 사용하는 함수 - range(시작숫자, 종료숫자)

# range에 인수로 하나의 숫자만 넣을 경우 시작은 0에서 종료 숫자-1 만큼의 range객체를 반환한다.
a = range(10)
print(a)

# range 함수의 사용
add = 0
for i in range(10):
    add += i
print(add)

# 0부터 10 미만의 숫자를 포함하기에 45가 나온다.
# 0부터 10까지의 숫자를 더하기 위해서는 range(11)을 넣어줘야한다.

#그래서 이 range의 사용법은 아래와 같이 사용할 수 있다.
marks = [86, 33, 55, 12, 44]

for i in range(len(marks)):
    print(marks[i])
    
#for 와 range를 사용한 구구단 
for i in range(2, 10):
    for j in range(1, 10):
        print("%d X %d = %d " %(i ,j ,i*j),  end="  ") # => end=" "를 넣으면 줄바꿈 대신 " "를 넣어준다. 
                                                       # end=" "의 내부에는 어떤 문자든 사용이 가능하고 print문이 끝날때마다 줄바꿈대신 넣어준다 
    print("  ") # => 단의 구분을 위해 추가 

# 리스트 컴프리헨션 사용하기

# 아래와 같이 리스트에 어떤값을 for문을 통해서 추가하는 경우가 있는데 
a = [1, 2, 3 ,4]
result = []
for num in a:
    result.append(num*3)
print(result)

#이를 리스트 컴프리헨션을 사용하면 좀 더 간단하게 사용할 수 있다.
a = [1, 2, 3, 4]
result = [num * 3 for num in a ]
print(result)

#만약 [1, 2, 3, 4] 중에서 짝수에만 3을 곱하여 담고 싶다면 리스트 컴프리헨션 안에 ‘if 조건문’을 사용하면 된다.
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# 리스트 컴프리헨션의 문법은 다음과 같다.
# [표현식 for 항목 in 반복 기능 객체 if 조건문]
result = [ num * 3       # => 표현식(반환하고자 하는 결과를 도출하는 코드를 의미하는 듯 보임)
            for 
            num          # => 항목(리스트의 내부의 값을 for문을 통해 돌리기 위한 변수, 그냥 for 변수 in 리스트, 튜플..에서의 변수와 같음)
            in
            a            # => 반복 기능 객체(리스트, 튜플등 반복이 가능한 객체를 의미)
            if
            num % 2 == 0 # => 조건문(for문을 돌때 해당 조건에 따라서 표현식을 실행할지 여부를 결정함, true => 표현식을 실행 / false => 표현식을 실행하지 않음)
        ]

print(result)

# 리스트 컴프리헨션은 다수를 한번에 사용이 가능하다
result = [x * y for x in a 
                for y in a ]

print(result)

# 리스트 컴프리헨션
result = [n * 3 for n in a if n % 2 == 0 for n in a if n % 2 == 1]
print(result)

# 이 리스트 컴프리헨션의 결과를 기존 for문으로 변경하면 아래와 같다
result = []
for n in a:
    if n % 2 == 0:
        for n in a:
            if n % 2 == 1:
                result.append(n * 3)
# 다중으로 들어가는 for문은 그 자식으로 들어가게 되고 그 내부 가장 상단에 if 조건문이 붙는 형식이라고 보면 된다.

# 그럼 위에 1 ~ 4를 곱하는 예제를 기존 for문으로 변경하면 어떻게 될까 

# 컴프리헨션 사용 
result = [x * y for x in a 
                for y in a ]

# 기존 for 문 
result = []

for x in a :
    for y in a:
        result.append(x*y)
print(result)
