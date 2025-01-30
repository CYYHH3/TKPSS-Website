import requests
from bs4 import BeautifulSoup

def crawl():
    url = 'http://tkpss.edu.hk'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 在这里添加你的爬虫逻辑
    print(soup.title.string)

if __name__ == '__main__':
    crawl()