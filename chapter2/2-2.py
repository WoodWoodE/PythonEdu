# 문자열

#아래 변수 모두 문자열
a = "Life is Good"
b = """Life is Good"""
c = "a"
d = "234"
e = '123.4'

print(type(a) , type(b) , type(c) , type(e))

# """, ''', ", ' 모두 문자열을 만들어줌

# escape 문자 \(백 슬래시)

f = ' I\'m Tester'
print(f)

# 줄 바꿈 문자 없이 여러 줄을 인식 시키기 위한 """, ''' 
h = '''Hello!
Tester
'''
print(h)

# escape코드(\를 사용하는 문자들)
# \n - 문자열 안에서 줄을 바꿀때 사용
g = ' Hello \n Tester'
print(g)

# \t - 문자열 사이에 탭 간격을 줄 때 사용
i = ' Hello\tTester'
print(i)

# \r - 캐리지 리턴(줄바꿈 문자, 커서를 현재 줄의 가장 앞으로 이동)

# 4개가 더있으나 잘 안쓰임.

## 문자열 연산하기

# 문자열 더해서 연산하기

head = 'Python'
tail = ' is Good'

print(head + tail)

# 문자열 곱하기

print(head * 3)

# 문자 곱하기는 문자 * 숫자 만 가능함, 문자 * 문자는 불가능함
#print(head * head) #에러

# 문자열 곱하기 응용
print('=' * 50)
print("My Program")
print("=" * 50)

# 문자열 길이 구하기 - len() 함수 
j = 'Life is Too Short'
print(len(j))

# 문자의 인덱싱과 슬라이싱
k = 'Life is Too Short, You need Enjoy'

# - 문자열 인덱싱 = 문자를 하나씩 뽑아옴, 인덱스는 0 부터 시작한다.
print(k[3])

# -- 인덱싱의 활용
print(k[0])
print(k[12])
print(k[-1]) # 거꾸로 찾음 -1부터 시작

print(k[0]+k[1]+k[2]+k[3]) # -> 인덱싱 방식

# - 문자열 슬라이싱 = 문자를 구간으로 뽑아옴 [이상:미만],  [이상:미만:간격]
print(k[0:4]) # -> 슬라이싱 방식
print(k[19:]) # ->  19번 이상부터 끝까지
print(k[::2]) # ->  처음부터 끝까지 2칸 간격으로 가져온다.
print(k[::-1]) # ->  끝부터 처음까지 1칸 간격으로 가져온다(거꾸로 찾아 가져옴).
print(k[::-2]) # ->  끝부터 처음까지 2칸 간격으로 가져온다(거꾸로 찾아 가져옴).

l = "20230441Rainy"
date = l[:8] # - 0~7번까지의 문자를 가져온다 
weather = l[8:] # - 8번~끝까지의 문자를 가져온다

print(date)
print(weather)

# 문자열 포매팅
# -- 문자열의 포멧을 정해놓고 특정 문자, 숫자와 같이 일부만 변경해서 사용하는것.
m = "I ate %d apples." % 3
print(m)

n = "I ate %s apples." % "three"
print(n)

#- 상수를 변수에 넣어 문자열 포매팅 사용 

o = '서른 마흔 다섯개'
p = "I ate %s apples." % o
print(p)

# - 두개 이상의 값 넣기 
number = 100
day = 'three'
q = "I ate %s apples, In %s days!" %(number ,day)
print(q)

# 문자열 포맷 코드 
# --- %s - 문자열 -> 이게 제일 중요함, 문자열은 모두 수용이 가능하기에..
# --- %c - 문자 1개
# --- %d - 정수
# --- %f - 부동소수
# --- %o - 8진수
# --- %x - 16진수
# --- %% - Literal % (문자 % 그 자체)

# 포맷 코드와 숫자 함께 사용하기 - %와 s 사이에 숫자가 들어가면 s에 해당하는 문자열을 포함해서 n개의 문자열을 출력시킨다. -> 거의 안씀
r = "%10s" % "Hi" # -> 빈칸 8개, 2개 문자
print(r)

s = "%s10" % "Hi" # 뒤에 숫자가 들어가면 그냥 출력됨
print(s)

# 만약 앞에 두고 싶다면 음수를 붙여주면 된다. -> 거의 안씀
t = "%-10stest" % "Hi"
print(t)

# 소수점 n번째 자리까지 표현해라
u = "%0.3f" % 3.434234 # -> 소수점 셋째자릿수 까지 표현해라, %.3f == %0.3f
print(u)

#잘은 안씀...

# format(n) 함수 - {index}안에 n을 넣는다
v = "I ate {0} apples.".format(3) 
print(v)

# 문자열도 동일하게 사용 가능, 0이라는것은 순서를 표현한 것이기에 궂이 문자열 숫자를 구분할 필요 없음
w = "I ate {0} apples.".format('three') 
print(w)

# 두개 이상의 값을 넣을 수도 있다.
x = "I ate {0} apples, Is was vary {1}".format('three',"bad")
print(x) 

# 변수를 넣어줄 수 도
day = "three"
mood = "king"
y = "I ate {0} apples, Is was vary {1}".format(day,mood)
print(y) 

# 변수 자체를 넣어줄 수 도 있다
z = "I ate {day} apples, Is was vary {mood}".format(day = 'three',mood = "good")
print(z) 

# 혼용도 가능하다
a = "I ate {0} apples, Is was vary {mood}".format('fives',mood = "So-so")
print(a)

# 왼쪽 정렬, 오른쪽 정렬 -> 거의 안씀, 이런게 있다 정도
a = "{0:<10}".format("hi") # {0:<10} => 총 10글자인데 <왼쪽 정렬하고 싶다
print(a)
a = "{0:>10}".format("hi") # {0:>10} => 총 10글자인데 >오른쪽 정렬하고 싶다 
print(a)
a = "{0:^10}".format("hi") # {0:^10} => 총 10글자인데 ^중앙 정렬하고 싶다 
print(a)
a = "{0:=^10}".format("hi") # {0:=^10} => 총 10글자인데 ^중앙 정렬하고 좌우로 빈공간을 =로 채운다. 
print(a)

# 소수점 표현하기 
y = 3.4124123
a = "{0:0.4f}".format(y) # {0:0.4f} => 소수점 4번째 자리까지 y를 출력해라
print(a) 

#{ 또는 } 문자 표현하기 - {와 }를 표현하기 위함 {{과 }}를 입력하면 {와 }가 출력됨
a = "{{ and }}".format()
print(a)

# f 문자열 포매팅
#파이썬 3.6 버전 부터는 f 문자열 포매팅 기능을 사용할 수 있음.

name = '홍길동'
age = 30
a = f'나의 이름은 {name}입니다. 나이는 {age}살 입니다.'
print(a)

#이것 또한 문법은 비슷하게 나옴, 중괄호 내부에서 연산이 가능하다
name = '홍길동'
age = 30
a = f'나의 이름은 {name}입니다. 나이는 {age+6}살 입니다.'
print(a)

# 정렬
a = f'{"hi":<10}'
print(a)
a = f'{"hi":>10}'
print(a)
a = f'{"hi":^10}'
print(a)
a = f'{"hi":=^10}'
print(a)

# 소수점
y = 3.424124
a = f'{y:0.3f}'
print(a)

## GPT 쓰라고 함 ㅋㅋ...

# 문자열 관련 함수들 

# 문자열 개수 세기(count)
# String.count("문자") 문자열에 해당 문자가 몆개가 존재하는지를 확인
a = 'hobby'
print(a.count('b'))

# 문자열 위치 확인(find)
# String.find("문자") 문자열에 해당 문자가 몆번째에 존재하는지를 확인(가장 처음 만나는 문자위치를 반환) - 0부터 시작
# 존재하지 않는 경우는 -1을 반환한다.
a = 'hobby'
print(a.find('b')) 
print(a.find('X')) 

# 문자열 위치 확인(index)
# String.index("문자") 문자열에 해당 문자가 몆번째에 존재하는지를 확인(가장 처음 만나는 문자위치를 반환) - 0부터 시작
# 존재하지 않는 경우는 에러를 발생시킨다
a = 'hobby'
print(a.index('b')) 
#print(a.index('X')) 

# 문자열 삽입(join)
# "문자".join(String) String의 사이사이에 문자를 넣어준다
a = ', '.join("asdf") # - a와s와d와f 사이에 ,를 넣어준다.
print(a)

#List도 가능하다.
a = ', '.join(["a","s","d","f"]) # - a와s와d와f 사이에 ,를 넣어서 하나의 문자열로 반환한다.
print(a)

#소문자를 대문자로 변경하기
# String.upper()
a = 'hi'
print(a.upper())

#대문자를 소문자로 변경하기
# String.lower()
a = 'HI'
print(a.lower())

#왼/오른/양쪽 공백지우기

# 왼
a = " hi " 
print(a.lstrip())

# 오른
print(a.rstrip())

# 양
print(a.strip())


# 문자열 바꾸기(replace())
a = "Life is too short."
print(a.replace("is", "are"))

# 문자열 나누기(split())
a = "Life is too short."
print(a.split())
print(a.split("i")) # 문자를 넣으면 해당 문자를 기점으로 잘리고, 해당 문자는 제거되면서 잘린다.
print(a.split("is")) # 문자를 넣으면 해당 문자를 기점으로 잘리고, 해당 문자는 제거되면서 잘린다.

# 문자를 넣었을때를 좀더 쉽게 보는 예
a = "a:b:c:d"
print(a.split(":"))

##문자형 자료형 끝##