# 패키지
# 파이썬에서 패키지(packages)란 관련 있는 모듈의 집합을 말한다. 
# 패키지는 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해 준다.

## 파이썬에서 모듈은 하나의 .py 파일이다.

# 파이썬 패키지는 디렉터리와 파이썬 모듈로 이루어진다. 
# 다음은 필자가 임의로 그려 본 game이라는 파이썬 패키지의 구조이다.

# 가상의 game 패키지 예
# game/
#     __init__.py
#     sound/
#         __init__.py
#         echo.py
#         wav.py
#     graphic/
#         __init__.py
#         screen.py
#         render.py
#     play/
#         __init__.py
#         run.py
#         test.py

# game, sound, graphic, play는 디렉터리, 확장자가 .py인 파일은 파이썬 모듈이다.
# game 디렉터리가 이 패키지의 루트 디렉터리, sound, graphic, play는 서브 디렉터리이다.

# 간단한 파이썬 프로그램이 아니라면 이렇게 패키지 구조로 파이썬 프로그램을 만드는 것이 공동 작업이나 유지 보수 등 여러 면에서 유리하다. 
# 또한 패키지 구조로 모듈을 만들면 다른 모듈과 이름이 겹치더라도 더 안전하게 사용할 수 있다.

#### __init__.py 파일은 조금 특이한 용도로 사용하는데, 뒤에서 자세하게 다룬다

##################
# 패키지 만들기
# 이제 위 예와 비슷한 game 패키지를 직접 만들어 보면서 패키지에 대해서 알아보자.

# 1. C:/doit 디렉터리 밑에 game 및 기타 서브 디렉터리를 생성하고 .py 파일들을 다음과 같이 만들어 보자(만약 C:/doit 디렉터리가 없다면 먼저 생성하고 진행하자).

# C:/doit/game/__init__.py
# C:/doit/game/sound/__init__.py
# C:/doit/game/sound/echo.py
# C:/doit/game/graphic/__init__.py
# C:/doit/game/graphic/render.py

# 2. 각 디렉터리에 __init__.py 파일을 만들어 놓기만 하고 내용은 일단 비워 둔다.

# 3. echo.py 파일의 내용은 다음과 같이 작성한다.

# # echo.py
# def echo_test():
#     print("echo")

# 5. 다음 예제를 수행하기 전에 우리가 만든 game 패키지를 참조할 수 있도록 명령 프롬프트 창에서 set 명령어로 PYTHONPATH 환경 변수에 C:/doit 디렉터리를 추가한다. 
#    그리고 파이썬 인터프리터를 실행한다.

# C:\> set PYTHONPATH=C:/doit
# C:\> python

# 여기까지 준비가 되었다면 다음을 따라 해 보자.

#**** 다음에 나올 실습은 반드시 명령 프롬프트에서 파이썬 인터프리터를 실행하여 진행해야 한다. 
#     많은 독자가 IDLE 셸 또는 비주얼 스튜디오의 파이썬 셸에서 다음 예제를 실행하다가 오류를 만난다.

##########################
# 패키지 안의 함수 실행하기
# 이제 패키지를 사용하여 echo.py 파일의 echo_test 함수를 실행해 보자. 패키지 안의 함수를 실행하는 방법에는 3가지가 있다. 
# 다음은 import 예제이므로 하나의 예제를 실행하고 나서 다음 예제를 실행할 때는 반드시 인터프리터를 종료하고 다시 실행해야 한다. 
# 인터프리터를 다시 시작하지 않을 경우, 이전에 import한 것들이 메모리에 남아 있어 엉뚱한 결과가 나올 수 있다.

# 첫 번째는 echo 모듈을 import하여 실행하는 방법으로, 다음과 같이 실행한다.

## echo 모듈은 echo.py 파일이다.
# >>> import game.sound.echo
# >>> game.sound.echo.echo_test()

# 두 번째는 echo 모듈이 있는 디렉터리까지를 from ... import하여 실행하는 방법이다. 
# 앞에서 import한 모듈 때문에 오류가 발생할 수 있으므로 인터프리터를 다시 시작한 후 다음 소스를 입력하자.

# >>> exit()
# C:\> python
# >>> from game.sound import echo
# >>> echo.echo_test()
# echo

#세 번째는 echo 모듈의 echo_test 함수를 직접 import하여 실행하는 방법이다.

# >>> from game.sound.echo import echo_test
# >>> echo_test()
# echo

# 하지만 다음과 같이 echo_test 함수를 사용하는 것은 불가능하다.

# >>> import game
# >>> game.sound.echo.echo_test()
# Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
# AttributeError: 'module' object has no attribute 'sound'

# import game을 수행하면 game 디렉터리의 __init__.py에 정의한 것만 참조할 수 있다.

# 또 다음처럼 echo_test 함수를 사용하는 것도 불가능하다.

#>>> import game.sound.echo.echo_test
# Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'game.sound.echo.echo_test'; 'game.sound.echo' is not a package

# 도트 연산자(.)를 사용해서 import a.b.c처럼 import할 때 가장 마지막 항목인 c는 반드시 모듈 또는 패키지여야만 한다.

######################################
#__init__.py의 용도
# __init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려 주는 역할을 한다. 
# 만약 game, sound, graphic 등 패키지에 포함된 디렉터리에 __init__.py 파일이 없다면 패키지로 인식되지 않는다.

#### python 3.3 버전부터는 __init__.py 파일이 없어도 패키지로 인식한다(PEP 420). 
#### 하지만 하위 버전 호환을 위해 __init__.py 파일을 생성하는 것이 안전한 방법이다.

# 또한, __init__.py 파일은 패키지와 관련된 설정이나 초기화 코드를 포함할 수 있다. 
# 다양한 방법으로 활용할 수 있는데, 몇 가지 예를 들어 살펴보자.

#### 다음에 나오는 예제는 __init__.py 파일을 수정한 후 반드시 파이썬 인터프리터를 종료하고 다시 실행해야 한다.

#####################################
# 패키지 변수 및 함수 정의
# 패키지 수준에서 변수와 함수를 정의할 수 있다. 
# 예를 들어, game 패키지의 __init__.py 파일에 공통 변수나 함수를 정의할 수 있다.

# # C:/doit/game/__init__.py
# VERSION = 3.5

# def print_version_info():
#     print(f"The version of this game is {VERSION}.")

# 이렇게 패키지의 __init__.py 파일에 정의된 변수와 함수는 다음과 같이 사용할 수 있다.

# >>> import game
# >>> print(game.VERSION)
# 3.5
# >>> game.print_version_info()
# The version of this game is 3.5.

#####################################
# 패키지 내 모듈을 미리 import
# __init__.py 파일에 패키지 내의 다른 모듈을 미리 import하여 패키지를 사용하는 코드에서 간편하게 접근할 수 있게 한다.

