class thailandpackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행\
(야시장 투어) 50만원")

#이 모듈이 어디서 온건지 알려주네 
if __name__== "__main__":
    print("thailand 모듈을 직접 실행한다는 뜻")
    print("이 문장은 모듈을 직접 실행할 때만 실행되요")
    trip_to = thailandpackage()
    trip_to.detail()
else:
    print("thailand 외부에서 모듈 호출")

        
