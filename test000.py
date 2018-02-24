from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com'
html = urlopen(url)
bs0bj = BeautifulSoup(html,'lxml')
download = bs0bj.findAll(src = True)
'''
#以'wb'模式 写入的文件     路径和名字
urlretrieve(imageLocation,'img\logo.jpg')
'''
for i in download:
    print(i['src'])
