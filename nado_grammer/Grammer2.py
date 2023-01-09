            ### 파이썬 기본문법정리2 ###

    #클래스란 붕어빵 틀!

class unit:
    def __init__(self,name,hp,damage,speed):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.speed = speed
        print("{0} 유닛이 생성 되었습니다.".format(self.name)) #self.name 말고 name와도 노상관
        print("체력 {0}, 공격력 {1}, 스피드 {2}".format(self.hp, self.damage, self.speed))
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
                .format(self.name, location, self.speed))
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다." .format(self.name))
marine1 = unit("마린", 40, 5,8)
marine1.move("3시") 
print(marine1.damage)

#이런 식으로쓰면 unit을 상속받는게 되는거지 unit:부모클래스, 이건 자식클래스.. 구조를 잘 봐
#부모클래스의 함수를 자식클래스의 개체가 attacker1.move이런식으로 사용가능
class attackunit(unit):
    def __init__(self,name,hp,damage,speed):
        unit.__init__(self, name, hp, damage, speed)
    def attack(self,location):
        print("{0}:{1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
            #여기에 있는 셀프들은 위 코드의 놈들이지. 

#자식클래스의 자식클래스도 문제없지
class marine(attackunit):
    def __init__(self):
        attackunit.__init__(self, "마린", 40, 5,1)
    def marine_speed(self):
        pass
    
#부모가 둘이상이 되는 다중상속!
#지상의 스피드는 가지고 오지 않기 위해 speed는 빼고 자리만 0으로 채워주는 모습
class flyattackunit(attackunit, flyunit): #클래스 flyunit있다치고
    def __init__(self,name,hp,damage,fly_speed): #내가 쓸 것들 딱 대려와서 def에서는 스피드를 적어주지않고
        attackunit.__init__(self, name,hp,damage,0)  #speed를 0으로 고정해주는 모습
        flyunit.__init__(self, fly_speed)       

class buildingunit(unit):
    def __init__(self,name,hp,location):
        unit.__init__(self, name, hp,0,0) #밑 줄 코드랑 똑같은 뜻
        # super().__init__(name, hp, 0) #윗 줄 코드랑 똑같은 뜻
        # 다중상속일때 super로 한꺼번에 받으면 괄호에서 첫번째순서만 받으니까
        # .__init__을 여러번 써서 다중상속을 받는것이 낫다.
        self.location = location

#메소드 오버라이딩
class person():
    def greeting(self):
        print("안녕하세요.")
class student(person):
    def greeting(self): #부모클래스와 자식클래스의 함수명이 같게해서! 우선권을 가져오는거지
        super().greeting() #부모클래스의 메소드호출하여 중복을 줄이는 방법도 있다.
        print("제 이름은 !입니다")

    #에러의 세계

#try문 : 신경쓰지말고 그냥돌리다가 에러가뜬다? > except문으로 이동의 구조
try:
    print("나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자 : "))
    num2 = int(input("두 번째 숫자 : "))
    an = int(num1/num2)
    print("{0}/{1}={2}".format(num1,num2,an))
    #숫자대신 문자를 input시키니 오류가 뜨네!
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
    #0을 넣었을땐 다른에러가 뜨네
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err) #에러의 종류까지 딱알려주는 끝판왕.. 이거하나만 써두됨

# 일부로 에러 발생시키기
try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자 : "))
    num2 = int(input("두 번째 숫자 : "))
    if num1 >= 10 or num2 >=10:
        raise ValueError #에러를 발생시키겟다
    an = int(num1/num2)
    print("{0}/{1}={2}".format(num1,num2,an))
except ValueError: #발생시킨 에러에 대한 처리
    print("잘못된 값을 입력. 한 자리 숫자만.")

# 에러를 정의하기, 상속을 이용
class bignumbererror(Exception): 
    def __init__(self, msg):
        self.msg = msg
    def __str__(self): #출력문을 구성하기위해 쓰는건데
        return self.msg #여기에선 역할이 딱히 없어서 생략가능
try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자 : "))
    num2 = int(input("두 번째 숫자 : "))
    if num1 >= 10 or num2 >=10:
        raise bignumbererror("입력값 : {0}, {1}".format(num1, num2))
    an = int(num1/num2)
    print("{0}/{1}={2}".format(num1,num2,an))
except ValueError:
    print("잘못된 값을 입력. 한 자리 숫자만.")
except bignumbererror as err:
    print("에러발생. 한 자리 숫자만.")
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err) #종류까지 딱알려주는 끝판왕
finally : #위에서 에러처리가 되든말든 발동
    print("계산기를 이용해줘서 고맙다")

    #모듈 : module

#파이썬파일을 모듈이라고 생각하면된다. 파이썬파일에서 다른 파이썬파일에있는
#함수를 사용하고 싶을때 .py는 때고
import Grammer1 #기본형태
Grammer1.profile(2) 
import Grammer3 as son #부르기 쉽게 변환가능
son.price(3)
from Grammer3 import * #온점 안찍고 price를 바로 쓸수 있다는 꿀팁
price(3)
from Grammer3 import price, price_morning #함수도 골라서만 사용가능
price(3)
price_soldier(5)
from module import price_soldier as price # 이렇게쓰면 솔저값을 price로 부르는 격
price(3) #솔저로 게산

    #패키지 : package

#패키지는 모듈의 모임 + __init__.py 파일
#import 문에서 맨 마지막 .의 개체는 모듈이나 패키지만 가능
#클래스나 함수는 직접적으로 import 할 수 없다.
#지금 바로밑에 형식은 패키지.모듈이 와 있네
import travel.thailand 
trip_to = travel.thailand.thailandpackage()
trip_to.detail()

#다만 from import 구문에서는 함수를 호출가능하다
from travel.thailand import thailandpackage
trip_to = thailandpackage() 
trip_to.detail()
from travel import vietnam
trip_to = vietnam.vietnampackage()
trip_to.detail()

#지금 이렇게 하면 오류가 나는데 모두 공개로 설정되어있지 않아서 그래.
#근데 init 파일에 코드를 작성하면 오류가 안나네 #travel의 init파일 확인!!
from travel import *
trip_to = vietnam.vietnampackage()
trip_to.detail()

#모듈의 저장위치를 알려주는 코드
import inspect
import random
from travel import *
print(inspect.getfile(random))
print(inspect.getfile(thailand))
#travel폴더를 복사해서 random이 저장되어있는 폴더를 열었어
#거기에 붙여넣기를 했음. random모듈처럼 travel폴더의 함수들도 쓸수있게된거임

    #pip의 모든것

#이미 쓰이고있는 패키지를 이용하는게 훨씬 효율적이다
#네이버에 pypi로 들어가보면 엄청난 패키지 검색가능
#터미널에서 pip install beautifulsoap4먼저 진행
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
#터미널에 pip list를 입력시켜보면 컴퓨터에 어떤 패키지가 깔려있는지~
#pip show beautifulsoup4하면 정보가 쫘악
#만약 업그레이드가 필요하다? pip install --upgrade beautifulsoup4 이렇게

# 내장함수에 대해서.. 따로 import 하지않아도 되는것은 당연~
input : 사용자 입력을 받는 함수
dir : 해당객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random #'외부함수'를 import해온 것이지.
print(dir()) #random이 추가됫네
print(dir(random)) #import된 random안에는 또 어떠한 것들이 있는지..
first = [1,2,3]
print(dir(first)) #리스트에 내제된 함수들.. 이런식으로

# 외장함수에 대해서..웹에서 찾아보는게 베스트. random이 예시
from random import *
date=randint(4,28)
print("스터디 모임 날짜는 매월"+str(date)+"일로 선정되었습니다.")
# glob : 경로 내의 폴더,파일 목록조회 dir과 같다
import glob
print(glob.glob("*.py"))
# os : 운영체제에서 제공하는 기본기능
import os
print(os.listdir()) #얘도 glob랑 비슷하다고만 알아둬
print(os.getcwd()) #현재 파일위치를 표시
# 경로를 바꿔주려면 os.chdir("~")사용. 터미널의 cd랑 같은기능
folder="sample"
if os.path.exists(folder):
    print("이미 존재하는 폴더입니다")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성하였습니다")
# 시간 관련함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
import datetime
print("오늘 날짜는", datetime.date.today())
today=datetime.date.today()
td=datetime.timedelta(days=100) #100일차이
print("우리가 만난지 100일은", today + td)

