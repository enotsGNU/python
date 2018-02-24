import requests
from bs4 import BeautifulSoup

def url_open(url):
    head = {#'Accept':'',
            #'Accept-Encoding':'gzip, deflate',
            #'Accept-Language':'zh-CN,zh;q=0.9',
            #'Connection':'keep-alive','DNT':'1',
            'Referer':'https://movie.douban.com/top250',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/63.0.3239.132 Safari/537.36'
            }
    try:
        req = requests.get(url,headers = head,timeout = 3)
    except:
        return None
    
    return req

def find_movies(html):
    movies =[]
    soup = BeautifulSoup(html.text,'lxml')
    targets = soup.find_all('div',class_ = 'hd')
    for each in targets:
        movies.append(each.a.span.text)
    print(movies)
    return movies

def find_pages(html):
    soup = BeautifulSoup(html.text,'lxml')
    targets = soup.find('span',class_ = 'next').previous_sibling.previous_sibling.text
    return int(targets)
    
url = 'https://movie.douban.com/top250'
res = url_open(url)
num = find_pages(res)

result = []
for i in range(num):
    print(i)
    html = url +'?start=' + str(25*i)+'&filter='
    html = url_open(html)
    result.extend(find_movies(html))


with open('top250.txt','w',encoding = 'utf-8') as f:
    for each in result:
        f.write(each+'\n')

