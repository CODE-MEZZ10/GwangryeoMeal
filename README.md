# GwangryeoMeal
semi_module 파일 추가
semi_module 파일 사용법
semi_module.py 를 열어 학교코드(sc) 와 시도교육청 코드(msc)를 설정
!!!예제 코드!!!
from semi_module import show_meal
print(show_meal())
★코드의 간편성 확대


pymeal.py 사용법
pymeal.py에서는 학교 고유번호와 시도교육청 코드와 날짜가 필요합니다
(학교 코드와 시도교육청 코드는 open.neis.go.kr 에서 확인가능합니다 날짜의 경우 형식은 YYYYMMDD 로 해야합니다 날짜의 형식이 맞지 않을경우 오류가 발생할수도 있습니다)
!!!예제 코드!!!
from pymeal import getmeal
sc = 학교코드
msc = 시도교육청 코드

today_meal = getmeal(sc, msc, 20231212)
print(today_meal)

모르는것이 있을경우에 leejr2127@proton.me로 문의 주세요


