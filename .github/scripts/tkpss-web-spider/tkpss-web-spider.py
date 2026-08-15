import requests, os, re
from bs4 import BeautifulSoup

def spider():
    # 爬取网页
    url = 'http://tkpss.edu.hk'
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    html = response.text

    # 删除 HTML 中的 sid 参数
    # 使用正则表达式匹配并删除所有 sid 参数
    html = re.sub(r'[?&]sid=[^&"]+', '', html)
    # 如果删除 sid 参数后 URL 以 & 结尾，则删除末尾的 &
    # html = re.sub(r'&$', '', html)

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.title.string)

    # 将爬取的内容保存到文件
    if not os.path.exists("origin"):
        os.makedirs("origin")
    with open("origin/tkpss.html", 'w', encoding='utf-8') as file:
        file.write(html)

if __name__ == '__main__':
    spider()