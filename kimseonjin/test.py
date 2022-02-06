'''
클래스 명 : 유저 클래스

설명 : 유저 클래스를 구현햇습니다.
함수는 이름을 가져오는 뭐가 있구요 뭐뭐를 위해서 만들었습니다.

작성일 : 2022.00.00

마지막 수정한 사람 : 김선진

마지막 수정한 날자 : 2022.00.00

Todo > 차후 이름을 반환하기 위한 함수를 구현해야 합니다.

Fixme > 지금 학년을 반환 대신 출력합니다. 차후 string으로 반환해야 합니다.

'''

class User(): # CamelCase

    def __init__(self) :
        self.user_name # pascal cass
        self.user_age

    def getName(self): # snake case
        pass

    def getGrade(self):

        if not self.user_age > 7 :
            print("유치원생 입니다.")
        
        if not self.user > 13 :
            print("초등학생 입니다.")

        if not self.user > 16 :
            print("중학생 입니다.")
        
        if not self.user > 19 :
            print("고등학생 입니다.")
        
        if not self.user > 16 :
            print("성인 입니다.")

"""

1. 네이밍 규칙
함수는 snake
클래스 명 camel
변수 명 파스칼

2. 주석
최상단 : todo, fixme
각 주석 위에 : 주석

3. if문 처리 :
if not 을 써서 indent를 관리하자! <- 권장 사항

4. 깃허브에 올릴 때, 최대한 자잘하게!

나중에 기업가면 코드 리뷰 <- 기능별

코드 길이가 100줄 <- 욕먹어요

한번 커밋 or push를 최대한 1~2개 내로
코드 수정은 10줄 내로

"""