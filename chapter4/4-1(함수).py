#함수

# 파이썬의 기본 함수구조
    
# def 함수명(매개변수):
#     수행할 문장1
#     수행할 문장2

#def는 함수를 만들때 사용하는 예약어, function과 같은 기능을 하는듯 보임
# 그냥 생각하기엔 definition의 약자로 보임

#간단한 함수를 생성해보자.

def add (a, b):
    return a + b 

# 이 함수의 이름은 add 이며 입력으로 2개의 값을 받아서 리턴값은 두 입력을 더한 값을 반환한다.

# 함수의 사용법
a = 1
b = 2
c = add(a, b)
print(c)

# 매개변수와 인수 
# 매개변수(parameter)와 인수(arguments)는 혼용해서 사용하는 용어이므로 잘 기억해 두자. 
# 매개변수는 함수에 입력으로 전달된 값을 받는 변수, 인수는 함수를 호출할 때 전달하는 입력값을 의미한다.

def add(a, b):  # a, b는 매개변수
    return a+b

print(add(3, 4))  # 3, 4는 인수

# 매개변수를 지정하여 호출하기
# 함수를 호출할 때 매개변수를 지정할 수 도 있다.

def sub( a, b ):
    return a - b

result = sub(a=5, b=3)
print(result)
# 사실 용도는 별로 없겠지만 이 경우는 순서에 상관없이 사용이 가능하다는 점이 있다.
result = sub(b=3, a=5)
print(result)

#입력값이 몇개가 될 지 모를 때 

# def 함수명(*매개변수):
#     수행할 문장

def add_many ( *args):
    result = 0
    for i in args :
        result += i
    return result

a = add_many(1,2,3,4,5,6,7,8,9,10)
print(a)

print("{0:=^10}".format("="))
#여러 개의 입력을 처리할 때 def add_many(*args)처럼 함수의 매개변수로 *args 하나만 사용할 수 있는 것은 아니다.
def add_many ( type, *args):
    
    print(type)
    if type == "add":
        result = 0
        for i in args :
            result += i
    elif type == "mult":
        result = 1
        for i in args :
            result *= i
        
    return result

a = add_many("add",2,3)
print(a)
a = add_many("mult",2,3)
print(a)


# 파이썬에서 is와 ==는 비교 연산자이지만 서로 다른 목적으로 사용됩니다. 주요 차이점은 다음과 같습니다:

#   == (동등성 비교):
#   두 객체의 값이 같은지 비교합니다.
#   객체의 내용을 비교합니다.

#   is (동일성 비교):
#   두 객체가 메모리 상에서 같은 객체인지 비교합니다.
#   객체의 ID(메모리 주소)를 비교합니다.

# 주요 특징:

#   불변 객체(immutable)의 경우:

#   작은 정수, 일부 문자열 등은 파이썬이 최적화하여 같은 객체를 재사용할 수 있습니다.
#   이 경우 is와 ==가 같은 결과를 반환할 수 있습니다.

#   가변 객체(mutable)의 경우:

#   리스트, 딕셔너리 등은 내용이 같아도 다른 객체일 수 있습니다.
#   이 경우 ==는 True를, is는 False를 반환할 수 있습니다.

#키워드 매개변수, kwargs(kwargs는 ‘keyword arguments’의 약자이며 args와 마찬가지로 관례적으로 사용한다.)
# 키워드 매개변수를 사용할 때는 매개변수 앞에 별 2개(**)를 붙인다
# 이름 앞에 **을 붙이면 매개변수 kwargs는 딕셔너리가 되고 모든 Key=Value 형태의 입력값이 그 딕셔너리에 저장된다

def print_kwargs(**kwargs):
    print(kwargs)
    
print_kwargs(a=3)
print_kwargs(head="keyword",tail="arguments")


# 함수의 리턴값은 무조건 하나

#리턴값에 두개의 값을 쉼표, 를 이용해서 넣어보자.
def add_and_mult(a, b):
    return(a+b),(a*b)

result = add_and_mult(2,3);
print(result) # => 튜플을 반환함

#이는 a = 2 , 3 처럼 return 2, 3을 하면 기본 튜플의 생성법과 동일하기에 값을 튜플로 반환하게 된다.
# 이걸 두개의 변수에 담으려면 아래처럼 사용하면 된다.
resultHead, resultTail = add_and_mult(2, 3)
print(resultHead)
print(resultTail)

#그러면 return을 두번써서 두번 반환하면 어떤가?
def add_and_mult(a, b):
    return a+b 
    return a*b

#VSCode를 사용하면 결과를 보기 전에도 확인이 가능하겠지만 "코드에 접근할 수 없다" 라는 경고가 출력된다.
result = add_and_mult(2, 3)
print(result)

##첫 번째 return문에서 결과를 반환하고 함수를 종료시키기에 두번째 return문에는 접근할 수 없다.

###### 자바는 그냥 return문 자체를 두번 작성할 수 가 없음...다름.

# 매개변수에 초기값 미리 설정하기
def say_myself(name, age, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % age) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")
        
#이렇게 작성하면 man이라는 값을 넣지 않더라고 에러를 발생 시키지 않는다.
say_myself("홍길동",45)
say_myself("홍길동", 45, False)

#그런데 저런 방식으로 작성하기 위해서는 초기값을 넣어주는 매개변수를 가장 마지막에 넣어줘야만 한다 
# def say_myself(name, man=True, age ): 
#     print("나의 이름은 %s 입니다." % name) 
#     print("나이는 %d살입니다." % age) 
#     if man: 
#         print("남자입니다.")
#     else: 
#         print("여자입니다.")

# 기본값이 아닌 인수가 기본 인수를 따릅니다. => 에러가 발생한다.
# 이는  ‘초깃값이 없는 매개변수(age)는 초깃값이 있는 매개변수(man) 뒤에 사용할 수 없다’라는 뜻이다. 
# 즉, 매개변수로 (name, age, man=True)는 되지만, (name, man=True, age)는 안 된다는 것이다. 
# 초기화하고 싶은 매개변수는 항상 뒤쪽에 놓아야 한다는 것을 잊지 말자.

# 함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a = a +1

vartest(a)
print(a)

#vartest함수 내부에 작성한 a 는 외부에 있는 변수 a와 전혀 관계가 없다
#저 함수 내부에서만 사용되는 변수이다

## 함수 안에서 함수 밖의 변수를 변경하는 방법

# return으로 값을 반환해서 대입하는 방법
a = 1
def vartest(a):
    a = a +1
    return a 

a = vartest(a)
print(a)

# global명령어를 사용하는 방법 => 좋은 방법은 아님 
a = 1 
def vartest(): 
    global a
    a = a + 1

vartest()
print(a)

# Lambda 예약어
# Lambda는 함수를 생성할 때 사용하는 예약어로, def와 동일한 역할을 한다.
# 보통 함수를 한 줄로 간결하게 만들 때 사용한다. 
# 우리말로는 ‘람다’라고 읽고 def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다.

# Lambda예약어 기본 사용법
# 함수명 = lambda 매개변수1, 매개변수2, ... = 매개변수를 이용한 표현식

add = lambda a, b : a+b
result = add(1,2)
print(result)

# lambda로 만든 함수는 return없이도 표현식의 결과값을 return시킨다.
def add(a, b ):
    return a+ b 
result = add(1,2)
print(result)
# 와 동일하다.
