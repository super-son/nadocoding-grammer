          ### 파이썬 기본문법정리 ###
          
     # isinstance 함수
     
a="이건 정수형이지"
if isinstance(a, int):
    print("hi") 
else:
    print("int형은 아니지")

    #연산 줄임말

math=3
math+=3
math-=3
math*=3
math%=3

    #기본적인 내장함수 문법

python="python is amazing"
print(python[0].isupper())
print(len(python))
print(python.replace("python","java"))
#세컨드 "n"의 위치를 묻는 코드
print(python.index("n",python.index("n")+1))
print(python.find("n",python.find("n")+1))
# find는 출력값이 없으면 -1을
# index는 에러를 내버리는 차이점 
print(python.count("n")) #몇 번나왔는지 카운트

    #기본적인 내장함수 문법 2

print("hello"[:2])
print("hello"[:-2])
print("hello"[-2:])
a=input("사이트를 입력해주세요:") #input값은 str. 문자열로 저장한다.
b=a[7:]
c=b[:-4]
x=c[:3]+str(len(c))+str(c.count("e"))+"i"
print("사이트의 비밀번호는"+x+"입니다")
url="http://naver.com"
my_str=url.replace("http://","")
my_str=my_str[:my_str.index(".")]
password=my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
print(password)

    #대입법

print("나는 %d살입니다." %20)
print("나는 %s살과 %s살입니다." %("파이썬","발간"))
print("나는 {a}살,{b}살입니다".format(b="안녕",a="반가워"))
age=20
color = "빨간"
print(f"나는 {age}살,{color}살입니다")
name="손휘준"
print(f"저의 이름은 {name}입니다")
a="이거보다 끝판왕"
print("그냥 이걸로 {0}하는 걸로 결론. {1}없지?".format("대통합",a))

    #여백의 미

print('''백문이 불여일견
백견이 불여일타''')
print("백문이 불여일견\n백견이 불여일타")
#탈출문자 \이거를 앞에 써주면 문자그대로라는 뜻으로 해석
#바꾸려는 문장 끝에 \하나치고 엔터하면 줄바꿈. 여기 예시 x
print("저는 \"나도코딩\"입니다")
print('저는 "나도코딩"입니다')
#\n, \r, \b, \t은 예외 (탈출문자)
print("red apple\rpine") #커서를 맨 앞으로 둔다는 뜻
print("redd\bapple")#앞 글자 삭제
print("red\tapple")#탭의 기능
# print("red"\n"aplle") 이렇게 쓰는거 아니야!!!!!

    #자료형 1. 리스트

hello=[]
hello.append("hi")

    #자료형 2. 딕셔너리

cabinet= {3:"d",7:"ad"}
#키:밸류의 구조, 키가 문자열이도 가능
# print(cabinet[5]) #애는 오류가 나고
print(cabinet.get(5)) #애는 none이 찍힌다
#get(x)은 key x의 대응값을 주는데
#get(x,y)에서 key x값이 존재하지않는다면 y를반환해주는 함수.
print(cabinet.get(5,"이 키는 사용가능"))
# 딕셔너리의 문법에도 []이걸 당근쓰지 키 나올때!
del cabinet[3]
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())
cabinet.clear()

    #자료형 3. 튜플

# 튜플은 속도가 빠르지만 수정은 불가
menu=("돈까스","치즈까스")
print(menu[0])
print(menu[1])
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

    #자료형 4. 세트

# 세트 집합은 중복 안되고 순서가 없음
my_set = {1,2,3,3,3,3}
print(my_set)
java={"유재석","김태호","양세형"}
python=set(["유재석", "박명수"]) #둘다 타입은 set
print(java&python)
print(java.intersection(python)) # 교집합
print(java|python)
print(java.union(python)) # 합집합
print(java - python)
print(java.difference(python)) #차집합
python.add("김태호")
java.remove("유재석") #자료수정

    #자료구조의 변경

menu={"커피","우유","쥬스"} #타입:세트
menu=list(menu) #리스트로 변경
print(menu,type(menu)) 
menu=tuple(menu) #튜플로 변경
print(menu,type(menu))

    #랜덤과 자료구조의 변경 활용

from random import *
users = range(1, 21)
users = list(users)
shuffle(users)
winners = sample(users, 4)
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))

    #for의 기본활용

for waiting in range(5):
    print("대기번호 : {0}".format(waiting))

students = [1,2,3,4,5]
new=[]
for i in students:
    new.append(100+i)
#위 코드를 훨씬 간결하게 구성해보자.
students_2=[1,2,3,4,5] #튜플, 세트, 리스트 노상관
students_2=[i+100 for i in students_2] #개별요소를 새로운 리스트로
#위 코드에서 말이야 [~~~if i>3] 이런식으로 if도 뒤에 넣을수 있다는 사실
# i+100이외에도 len)i, i,upper()등 다양하게 활용
print(students_2)

    #while의 기본활용

customer = "토르"
index=5
while index >=1 :
    print("{0}님, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer,index))
    index -= 1
    if index==0 :
        print("커피 버려보리기")

    #루프 속 continue와 break의 활용

absent=[2,5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue #그 순번은 봐주고 다음순번으로 넘어가는것. pass는 아무일도 일어나지않는다는 것.
    elif student in no_book:
        print("수업 끝, {0}번 학생은 교무실로!".format(student))
        break #반복문 탈출
    print("{0}번 학생~, 책을 읽어봐".format(student))

    #def 함수정의

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission
    #여러값을 한번에 반환할수도 있다.
def profile(name, age=17, main_lang="python"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
        .format(name,age,main_lang))
profile("유재석")
# 여기서 함수값에 기본값을 걸어줄수도 있는데..
# 값을 입력받지 않으면 기본값을 송출해준다
def profile(name, age, lang1, lang2, lang3): # (age=20) 이런식으로
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3)
profile("유재석",20, "python","java","c")
# 끝에 end=""는 줄바꿈 \와 목적은 비슷하다.
# 할수있는 언어를 수정할때 함수자체를 바꿔야하므로
# 가변인자라는 개념을 도입한다.
def profile(name, age, *lang):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for i in lang:
        print(i, end=" ")
    print() #유재석과 김태호의 줄바꿈을 주기위해 공백을 주는거네 end=""를 소화하면서
profile("유재석",20, "python","java","c")
profile("김태호",25, "kotlin","c#")

    # 1부터 100 예쁘게 나열하기
    
for i in range(1,101):
    if i%10==0:
        print("{0}\n".format(i),end='')
    else:
        print("{0}".format(i),end=' ')

    #지역변수와 전역변수

gun=15
def check(soliders):
    # gun=10
    global gun #이게 없었다면 지역변수에 의해 오류가 남, 실제로는 오류날 확률 때메 잘 사용안함
              #전역 공간에 있는 gun을 사용하겠다는 뜻
    gun=gun-soliders
    print("남은 총 : {0}".format(gun))
    return gun #global 대신 이런식으로 외부와 접촉도 가능
gun=check(2)
print(gun)

    #출력문 표현

print("python","java","javascript",sep=" vs ") #여백에 삽입
print("python","java",sep=",",end="? ") #혼용
print("이어보이나요?")

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items() : #키와 밸류 pair로 가져온다
    #ljust(8)는 왼쪽으로 8개의 공간을 확보해서 정렬한다는 뜻
    print(subject.ljust(8),str(score).rjust(4), sep=":")

for num in range(1,21):
    #여기에 001, 002 이런식으로 채우고 싶다면
    #z.fill(3)은 3의 공간을 차지 후 값이 없는 곳에 0을 채운다
    print("대기번호 : " + str(num).zfill(3))

# 빈 자리는 두고, 오른쪽 정렬, 총 10자리의 공간 확보
print("{0: >10}".format(500))
# 양수일 땐 +, 음수일 땐 -
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(1000000000))
# 콤마 + 음양 표시하기
print("{0:+,}".format(-1000000000))
# 3자리콤마, 음양, 자릿수확보, 빈자리 채우기까지
print("{0:^<+30,}".format(1000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 특정자리수 까지 (셋째자리에서 반올림 해달라는 뜻)
print("{0:.2f}".format(5/3))

    #파일 쓰고읽기

#쓰기용 파일
score_file = open("score.txt", "w", encoding="utf-8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

#이어쓰기용 파일, append, 줄바꿈을 따로 명시해줘야되
score_file = open("score.txt", "a", encoding="utf-8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

#읽기용 파일
score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.read()) #파일에 있는 모든내용을 읽는다
score_file.close()

#줄별로 읽기, 한 줄 읽고 커서는 다음줄로 이동
#줄바꿈이 거슬린다면 readline(), end=""이걸 추가해주면 되지
score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.readline())
print(score_file.readline())
print(score_file.readline(),end="")
print(score_file.readline())
score_file.close()

# 반복문으로 한줄씩 다불러오기
score_file = open("score.txt", "r", encoding="utf-8")
while True : 
    line = score_file.readline()
    if not line:
        break
    print(line,end="")
score_file.close()

#리스트로 다불러오기
score_file = open("score.txt", "r", encoding="utf-8")
lines=score_file.readlines() #리스트형태로 저장
for line in lines:
    print(line, end="")
score_file.close()

#간단하게 파일쓰는법. 바이너리파일에도 적용가능
with open("soccer.txt","w",encoding="utf8") as data:
    data.write("이렇게 쉽게 되네")
#읽는것도 간단하게 두줄컷!! close도 안해줘도 되기때문
with open("soccer.txt","r",encoding="utf8") as data2:
    print(data2.read())

    #바이너리파일 쓰고읽기

import pickle #바이너리파일, 쓰기목적, 인코딩 따로 x
profile_file = open("profile.pickle","wb")
profile={"이름":"박명수","나이":30,"취미":
["축구","골프","코딩"]}
pickle.dump(profile, profile_file) #정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle","rb")
profile=pickle.load(profile_file) #file정보를 profile에 불러오기
print(profile)
profile_file.close()

#저 파일을 불러와서 hello라는 변수에 저장
with open("profile.pickle","rb") as hello:
    print(pickle.load(hello))