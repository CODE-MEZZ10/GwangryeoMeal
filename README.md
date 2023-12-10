# GwangryeoMeal
pymeal.py사용법
pymeal.py에는 getmeal이라는 함수가 존재합니다
getmeal 함수로 거의 모든 학교의 급식을 불러올수 있습니다
사용법 변수 = getmeal("학교 코드", "시도 교육청 코드", "날짜")
!!예제 코드 (오늘의 급식을 불러옴)
from pymeal import getmeal
from datetime import date

today = date.today()
sc = "학교 코드"
msc = "시도 교육청 코드"

todaymeal = getmeal(sc, msc, today)
print(todaymeal)
