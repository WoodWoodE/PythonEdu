# 딕셔너리
# 사전은 단어 - 뜻 의 쌍으로 이루어져 있는데 이런 형태의 데이터타입을 의미한다.
# 다른 언어에서는 Hash, Map, Object, JSON과 같은 포지션임.
# API에서 자주 활용됨

dic = {"name":"pay", "phone": "010-9999-2222", "birth":"1118"}
print(type(dic))

# 하나의 값만 존재할 경우 아래와 같이 표현한다.
dic = {"name":"hani"}
print(dic)

#value에 list를 넣을 수도 있다.
dic = {"a": [1, 2, 3]}
print(dic)

#============================

#딕셔너리 쌍 추가하기 - a[key] = value로 값을 추가할 수 있다.
a = {1 : "a"}
a[2] = 'b'
a["테스테스트"] = 'test'
a["배열테스트"] = [1, 2, 3]
print(a)

#리스트에선 index를 입력해서 해당 index의 값을 변경해줬는데 딕셔너리는 조금 다르다.

#딕션너리 쌍 삭제하기 - del 딕셔너리[key]를 넣으면 해당 키와 값 쌍이 삭제된다
a = {1 : "a", 2:"b", "name":"cherry", 3:[1, 2, 3]}
del a["name"]
#del에는 여러개를 ,로 나열하면 한번에 삭제도 가능하다
del a[1], a[2]
print(a)

#딕셔너리에서 key를 사용해서 value 얻기
a = {1 : "a", 2:"b", "name":"cherry", 3:[1, 2, 3]}
print(a[1])
print(a["name"])
print(a[3])
#없는것을 가져오려고 하면 오류가 발생함

# 딕셔너리를 만들때 주의사항 - key가 중복되면 안됨, key를 변경할 수 없음
#=====================================================================

# key 리스트 만들기 - keys()
a = {"name":"pay", "phone": "010-9999-2222", "birth":"1118"}
print(a.keys())
#dict_keys로 출력되는데 이는 예전 파이썬에서는 그냥 List로 나왔었음
#근데 List보다 좀 더 메모리를 덜 차지하는 형태
# 이는 반복문이랑 보통 같이 쓰이기 마련이기 때문임..
# 특징은 List와 비슷하나 간략함

for b in a.keys() :
    print(b)

# value 리스트 만들기 - values()
a = {"name":"pay", "phone": "010-9999-2222", "birth":"1118"}
print(a.values())

#key와 value를 한번에 얻기 - items()
a = {"name":"pay", "phone": "010-9999-2222", "birth":"1118"}
print(a.items())
# 리스트 내부에 튜플 형태로 key,value쌍으로 넣어서 출력해줌

#key, value쌍 모두 지우기 - clear()
a = {"name":"pay", "phone": "010-9999-2222", "birth":"1118"}
print(a.clear())
# 그냥 모든 값을 지운다.

#딕셔너리에서 값을 가져올때는 a['key']뿐 만 아니라 get이라는 메서드도 사용이 가능하다.
a = {"name":"pay", "phone": "010-9999-2222", "birth":"1118"}
print(a['name'])
print(a.get('name'))
# 이 둘의 차이는 없는 key를 사용할때 발생한다
#print(a['test']) # => 에러발생
print(a.get('test')) # => None이라는 값이 출력됨

#get을 응용해볼 수 도 있음.
# 만약 값이 없으면 뭘 반환할지도 작성해줄 수 가 있다
print(a.get("test","값이 읎습니다")) # => key가 존재하지 않아 "값이 읎습니다" 반환
print(a.get("name","값이 읎습니다")) # => key가 존재해서 value 반환

# 해당 key값이 딕셔너리 안에 존재하는지를 확인하는 것도  가능하다
print("name" in a) # => boolean 값, true/false로 값을 반환함


