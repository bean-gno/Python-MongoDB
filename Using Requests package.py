import requests

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

gus = rjson['RealtimeCityAir']['row']

#IDEX_MVL이라는 미세먼지 수치가 60보다 낮은 '구'들을 출력
for gu in gus:
    if gu['IDEX_MVL']<60:
        print(gu['MSRSTE_NM'], gu['IDEX_MVL'])
