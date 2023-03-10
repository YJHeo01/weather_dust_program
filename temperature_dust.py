import requests
import json
import sqlite3
import datetime



def getAirQualityByCity(city, key):
    endpoint = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
    url = f"{endpoint}?sidoName={city}&pageNo=1&returnType=json&numOfRows=100&serviceKey={key}&ver=1.0"
    res = requests.get(url)
    return res

def getWeather(X,Y):
    global temperature
    now = datetime.datetime.now()
    year = int(now.year)
    month = int(now.month)
    day = int(now.day)
    hour = int(now.hour)
    base_time = hour*100
    if(base_time<1000):base_time = "0" + str(base_time)
    base_date = 10000*year+100*month+day
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    params ={"serviceKey" : '', "pageNo" : "1", "numOfRows" : "1000", "dataType" : "json", "base_date" : str(base_date), "base_time" : str(base_time), "nx" : str(X), "ny" : str(Y) }
    response = requests.get(url, params=params)
    #print(response.content)
    response_body = response.json()["response"]["body"]["items"]
    for item in response_body["item"]:
        if(item["category"] == "T1H"):
            temperature = float(item["obsrValue"])
            print(f"현재 온도는 {temperature}도 입니다. ")
            if(temperature>20):print("반팔, 반바지를 추천합니다.")
            elif(temperature<10):print("추우니 옷을 따뜻하게 입으세요.")
            else:print("날이 선선합니다. 입고 싶은데로 입으세요.")


    

def getSection(dong):
    conn = sqlite3.connect("map.db")
    curs = conn.cursor()
    XY = curs.execute(f"Select * from Map where Dong='{dong}'")
    tmp=XY.fetchall()[0]
    conn.commit()
    conn.close()
    X = tmp[2]
    Y = tmp[3]
    Section = tmp[1]
    getWeather(X,Y)
    return Section

def kf_mask_cal(dust):
    if(dust<80):return 0
    if(dust<150):return 80
    if(dust<500):return 94
    return 99

    
if __name__ == '__main__':
    kf_mask = 0
    dong = input("궁금한 동을 입력해주세요. : ")
    city="인천"
    key = ""
    Section=getSection(dong)
    response = getAirQualityByCity(city,key)
    if(response.status_code == 200):
        response_body = response.json()['response']['body']
        for item in response_body['items']:
            if(item['stationName'] == Section):
                print(f"현재 공기의 PM10는 {item['pm10Value']} ug/m3입니다.")
                kf_mask = kf_mask_cal(int(item['pm10Value']))
        if(kf_mask == 0):
            print('KF 마스크를 쓰실 필요는 없습니다.')
        else:
            print(f"KF{kf_mask} 마스크 착용을 권장합니다.")

    else:
        print(f'Error code: {response}')  
