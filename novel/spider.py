#this is spider
import requests
import re
#from bs4 import BeautifulSoup

#get html page
def get_html(url):
    header = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0"}
    html = requests.get(url, headers =  header,timeout = 50 )
    return html

def get_urls(url):
    html = get_html(url).text
    rule = re.compile(r'https://www.x23us.com/html/[0-9]{2}/[0-9]{5}')
    urls = rule.findall(html)
    #print(urls)
    with open('url','a') as f:
        for i in urls:
            f.write(i)

def start():
    urls = []
    urlbase = 'https://www.x23us.com/'
    for i in range(1,11):
        urls =[]
        url = urlbase + 'class/' + str(i) + '_1.html'
        urls.append(url)
        for a in range(1,int(getmaxpage(url))):
            newurl = urlbase + 'class/' + str(i) + '_' + str(a) + '.html'
            urls.append(newurl)
    for url in urls:
        get_urls(url) 
    
def getmaxpage(urls):
    getnum = re.compile(r'class="last">([0-9]{1,3}){1}.+')
    html = get_html(urls).text
    maxnum = getnum.findall(html)
    print (str(maxnum[0]))
    return str(maxnum[0])
if __name__ == '__main__':
    url = 'https://www.x23us.com/class/6_1.html'
    #getmaxpage(url)
    start()
