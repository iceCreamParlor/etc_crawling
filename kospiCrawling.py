import urllib.request
import requests
import urllib.parse
import bs4


req = requests.get('http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=100/')
# HTML 소스 가져오기

html = bs4.BeautifulSoup(req.text, 'html.parser')
print(html.find_all('dt'))
