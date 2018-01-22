# 실습1. 미세먼지 정보 활용하기
import requests
url = "http://openapi.seoul.go.kr:8088/54775266536e6564393578574d4c41/json/TimeAverageAirQuality/1/25/201801171700"
response_body = requests.get(url).json()

dust = int(response_body['TimeAverageAirQuality']['row'][0]['PM10'])

# 1. dust 변수에 담겨 있는 미세먼지 농도 값 출력하기

# 2. 조건문을 활용하여 미세먼지 농도에 따른 미세먼지 상태 출력하기
