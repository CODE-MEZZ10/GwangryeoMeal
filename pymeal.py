import http.client
import json

def getmeal(sc, msc, date):
    url = "/hub/mealServiceDietInfo"

    headers = {
        "Content-type": "application/json",
    }

    conn = http.client.HTTPSConnection("open.neis.go.kr")
    payload_today = {
        "KEY": "c3bfcbc6be3548ea975dde21061bee96",
        "Type": "json",
        "pIndex": 1,
        "pSize": 1,
        "ATPT_OFCDC_SC_CODE": msc,
        "SD_SCHUL_CODE": sc,
        "MLSV_YMD": date,
    }

    conn.request("GET", url + "?" + "&".join([f"{key}={value}" for key, value in payload_today.items()]), headers=headers)
    response_today = conn.getresponse()
    data_today = response_today.read()

    try:
        meal_data_today = json.loads(data_today)["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"]
        cleaned_info_today = "\n".join(''.join(c for c in line if c not in '()0123456789.').strip() for line in meal_data_today.split("<br/>"))
    except KeyError:
        cleaned_info_today = "Can't acess to info"

    conn.close()
    return cleaned_info_today
