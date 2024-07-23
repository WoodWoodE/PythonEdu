#while문

# while문의 기본 구조 

# while 조건문:
#     실행할 코드1
#     실행할 코드2
#     실행할 코드3
#     ...

#while문은 조건이 거짓이 될때까지 계속 코드를 실행시킨다.

# 열번찍어 안넘어가는 나무 없다를 코드로 작성한다면 아래와 같이 된다.
pick = 0
while pick < 10:
    pick += 1
    print("나무를 %d번 찍었습니다." %pick)        
    if pick == 10:
        print("나무가 넘어갑니다.")


# 여러 선택지중 하나를 선택해서 입력받아보자. - input() => 사용자의 입력을 받는 함수 - Scanner().nextLine() 이거랑 비슷하다고보면 될듯 
prompt = '''
    1. Add
    2. Delete
    3. List
    4. Quit
    
    Enter Number:
'''

usrInput = 0
while usrInput != 4:
    print(prompt)
    usrInput = int(input());
    if usrInput < 1 or usrInput > 4 :
        print("숫자는 1 ~ 4까지밖에 입력하실 수 없습니다")
        usrInput = 4
    else:
        if usrInput == 1:
            print("add")
        elif usrInput == 2: 
            print("Delete")
        elif usrInput == 3: 
            print("List")
        elif usrInput == 4: 
            print("Quit")
        

# while 문 강제로 빠져나가기 - break => 사용법 다르지 않음

# while 문의 첫문장으로 되돌리기(현재 횟차를 그냥 무시하고 다음회차로 이동) - continue => 사용법 다르지 않음

