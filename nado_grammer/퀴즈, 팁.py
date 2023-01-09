# def 서류심사():
#     print("1.서류심사") 
#     return True

# def 서류심사():
#     print("1.서류심사"); return True

# def 서류심사(): print("1.서류심사"); return True
################################################### 다 같은 것들

def 서류심사(): print("1.서류심사"); return True
def 신체검사(): print("2.신체검사"); return False
def 코딩테스트(): print("3.코딩테스트"); return True
def 최종면접(): print("4.최종면접"); return True

if 서류심사() and 신체검사() and 코딩테스트() and 최종면접():
    print("합격 축하드립니다")
else :
    print("아쉽게도 탈락입니다")
################################################### 개발에서도 많이 쓰는 형식이니 알아둬라

def three():
    print("three",end="")
    return 3

def five():
    print("five",end="")
    return 5

def seven():
    print("seven",end="")
    return 7

#quiz code
three()>five()>seven() #의 결과 값은?.. 바로 three five이다. > > 로 연결되있는건 위에 and조건과 똑같다 보면되고 five()까지 동작하고 멈췄잖니

