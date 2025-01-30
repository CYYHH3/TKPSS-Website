import requests
from bs4 import BeautifulSoup

def spider():
    url = 'http://tkpss.edu.hk'
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')

    # 在这里添加你的爬虫逻辑
    print(soup.title.string)

if __name__ == '__main__':
    spider()