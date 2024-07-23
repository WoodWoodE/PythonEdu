#파일 읽고 쓰기

#파일 생성하기 
# f = open("newFile.txt","w")
# f.close()

# 위 코드를 실행하면 파일이 하나 생성된 것을 볼 수 있다.
# 파일을 생성하기 위해서 open()이라는 파이썬 내장함수를 사용했다.
# open함수의 사용법은 아래와 같다

# 파일객체 = open("파일명","파일열기모드")

# 그리고 파일 열기 모드의 종류는 아래와 같다
# r => 읽기 모드 : 파일을 읽기만 할 때 사용한다
# w => 쓰기 모드 : 파일에 내용을 쓸 때 사용한다 => 기존에 파일이 존재하지 않으면 새 파일을 생성, 기존에 파일이 존재하면 내용을 갈음한다.
# a => 추가 모드 : 파일의 마지막에 새로운 내용을 추가할 때 사용한다

# 만약 파일을 현재 위치가 아니라 원하는 위치에 생성하고 싶다면 아래와 같이 사용해야한다.

# f = open("C:/Users/Administrator/Desktop/전체/업무외/python(jo)/pythonEdu/newFileSnd.txt","w")
# f.close()

# 루트를 역슬래시 \ 를 넣으려면 역슬래시를 두개씩 사용해줘야한다 C:/Users/Administrator/Desktop => C:\\Users\\Administrator\\Desktop
# 혹은 문자열 앞에 r문자(raw String)를 넣어서 사용해야한다. r"C:\Users\Administrator\Desktop" 
# 왜냐면 C:\note\Administrator\Desktop라는 위치라면 \note에서 \n을 개행문자로 인식할 수 있기 때문이다


##파일을 쓰기 모드로 열어 내용 쓰기 
# f = open(r"C:\Users\Administrator\Desktop\전체\업무외\python(jo)\pythonEdu\chapter4\newFile.txt","w")
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" %i
#     f.write(data)
# f.close()


#파일을 읽는 여러가지 방법

#readline 함수 이용하기
f = open(r"C:\Users\Administrator\Desktop\전체\업무외\python(jo)\pythonEdu\chapter4\newFile.txt","r")
# line = f.readline()
# print(line)
# f.close()

#만약 모든 줄을 읽어 화면에 출력하고 싶다면 아래와 같이 작성하면 된다.
f = open(r"C:\Users\Administrator\Desktop\전체\업무외\python(jo)\pythonEdu\chapter4\newFile.txt","r")
# while True:
#     line = f.readline()
#     if not line : break
#     print(line)
# f.close()

#readlines 함수 사용하기
f = open(r"C:\Users\Administrator\Desktop\전체\업무외\python(jo)\pythonEdu\chapter4\newFile.txt","r")
lines = f.readlines()
for line in lines : 
    print(line)
f.close()
#readlines 함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 가지는 리스트를 리턴한다
print(lines)

#줄 바꿈 문자 제거하기(\n 제거하기)
# 파일을 읽을때 줄 끝의 \n문자를 제거해야하는 경우가 꽤있다고 한다.
# 이럴때 strip()함수를 사용하면 줄 바꿈 문자를 제거할 수 있다.

#기존 lines는 개행이 되어 두줄씩 출력되는데, 이때 strip()함수를 사용해서 다시 만들면 
f = open(r"C:\Users\Administrator\Desktop\전체\업무외\python(jo)\pythonEdu\chapter4\newFile.txt","r")
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)
f.close()
#개행되지 않는 것을 볼 수 있다.

#read함수 사용하기
f = open(r"C:\Users\Administrator\Desktop\전체\업무외\python(jo)\pythonEdu\chapter4\newFile.txt","r")
data = f.read()
print(data)
f.close()
#f.read()는 파일의 내용 전체를 문자열로 리턴한다. 따라서 위 예의 data는 파일의 전체 내용이다

#파일 객체를 for 문과 함께 사용하기
f = open(r"C:\Users\Administrator\Desktop\전체\업무외\python(jo)\pythonEdu\chapter4\newFile.txt","r")
for line in f :
    print(line.strip())
f.close()
# 파일 객체(f)는 기본적으로 위와 같이 for 문과 함께 사용하여 파일을 줄 단위로 읽을 수 있다.

# 파일에 새로운 내용 추가하기
# 쓰기 모드('w')로 파일을 열 때 이미 존재하는 파일을 열면 그 파일의 내용이 모두 사라지게 된다. 
# 하지만 원래 있던 값을 유지하면서 단지 새로운 값만 추가해야 할 경우도 있다. 
# 이런 경우에는 파일을 추가 모드('a')로 열면 된다
f = open(r"C:\Users\Administrator\Desktop\전체\업무외\python(jo)\pythonEdu\chapter4\newFile.txt","a")
for i in range(11, 20):
    data = "%d번째 줄입니다\n" %i
    f.write(data) #=> write(내용) = 파일객체에 들어 있는 파일에 내용을 작성한다.
f.close()


# with 문과 함께 사용하기
# Python의 with 문은 리소스 관리를 위한 컨텍스트 매니저를 구현하는 편리한 방법입니다. 
# 주로 파일 처리, 데이터베이스 연결, 네트워크 소켓 등 사용 후 명시적으로 닫아야 하는 리소스를 다룰 때 사용됩니다.
f = open(r"C:\Users\Administrator\Desktop\전체\업무외\python(jo)\pythonEdu\chapter4\newFile2.txt","a")
f.write("Life is too short, you need python")
f.close()
#보통은 위와 같이 열었다가 닫는것을 볼 수 있다.
#with문은 열렸으면 자동으로 닫게끔 해준다.
with open(r"C:\Users\Administrator\Desktop\전체\업무외\python(jo)\pythonEdu\chapter4\newFile2.txt","a") as f:
    f.write("Life is too short, you need python")
#위와 같이 with 문을 사용하면 with 블록(with 문에 속해 있는 문장)을 벗어나는 순간, 열린 파일 객체 f가 자동으로 닫힌다.

## with문 
#자원을 획득하고, 반환해야할 경우 사용된다.

# with EXPRESSION [as VARIABLE]:
#	BLOCK


# with open("파일 패쓰/파일 명",'모드') as 해당 파일을 담을 객체 :
#    파일객체.write("파일 내용")

### with는 객체에 대해서 이해해야만 사용할 수 있음으로 보인다.

