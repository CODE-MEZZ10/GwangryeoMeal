# GwangryeoMeal
사용법:
string변수 = getmeal("학교 코드", "시도 교육청 코드", "날짜")

예제코드
from pymeal import getmeal
from datetime import date

today = date.today()
sc = "학교 코드"
msc = "시도 교육청 코드"

todaymeal = getmeal(sc, msc, today)
print(todaymeal)
