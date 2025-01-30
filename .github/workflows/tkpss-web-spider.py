import requests
from bs4 import BeautifulSoup

def spider():
    url = 'http://tkpss.edu.hk'
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')

    # 在这里添加你的爬虫逻辑
    print(soup.title.string)

    # 将爬取的内容保存到文件
    with open("tkpss.html", 'w', encoding='utf-8') as file:
        file.write(response.text)

if __name__ == '__main__':
    spider()