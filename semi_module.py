from pymeal import getmeal
from datetime import datetime

current_date = datetime.now().strftime("%Y%m%d")
sc = "9022116"
msc = "S10"

def show_meal():
    return getmeal(sc, msc, current_date)
