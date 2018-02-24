import requests
import re
import os
import time
#重大问题下载到65张图片就不动了原因竟然是文件名是局部变量一直重复覆盖 噗
#下载到15,243时不动了   Ctrl+C也没用不知道咋了   ip也没被屏蔽
#是因为超时
global filename 

def url_open(url):
    head = {#'Accept':'',
            #'Accept-Encoding':'gzip, deflate',
            #'Accept-Language':'zh-CN,zh;q=0.9',
            #'Connection':'keep-alive','DNT':'1',
            'Referer':'http://www.mzitu.com/',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/63.0.3239.132 Safari/537.36'
            }
    req = requests.get(url,headers = head,timeout = 3)
    
    return req

def get_page_adds(html):
    search = r'<a href="([^"]+\d+)" target="_blank">'
    page_adds = []
    for i in re.findall(search,html):
        if i in page_adds:
            continue
        else:
            page_adds.append(i)
    return page_adds

def get_page(url):
    html = url_open(url).text
    #print(html)
    '''
    想用正则表达式，结果根本不会。反正都有规律，直接下载吧
    search = r'<a .* href="([^"]+\d+)">'
    page_adds = re.findall(search,html)
    '''
    page = []
    #存储其他页的网址
    for i in range(1,31):
        if i == 1:
            adds = 'http://www.mzitu.com/mm/'
            page.append(adds)
        else:
            adds = 'http://www.mzitu.com/mm/page/'+str(i)+'/'
            page.append(adds)
    #print(page)
    page_adds = []
    temp = []
    for pa in page:
        urll = url_open(pa).text
        temp = get_page_adds(urll)
        page_adds += temp
    print('开始下载喽！！！！')
    print(len(page_adds))
    return page_adds


def get_image_adds(page_adds):
    for page in page_adds:
        html = url_open(page).text
        search = r'<span>(\d+)</span>'
        pg = re.findall(search,html)
        max_pg = pg[-1]
        #print(max_pg)每套图页数

        img_adds =[]
        for i in range(1,1+int(max_pg)):
            if i == 1:
                url = page
            else:
                url = page + '/' + str(i)
            #print(url)
            this = url_open(url).text
            search_jpg = r'<img src="([^"]+\.jpg)"'
            for j in re.findall(search_jpg,this):
                if j in img_adds:
                    continue
                else:
                    img_adds.append(j)
        print(img_adds)
        download(img_adds)
        time.sleep(1)
        #下载一套图
                 
def download(img_adds):
    global file_name 
    for each in img_adds:
        with open(str(file_name)+'.jpg',"wb") as f:
            img = url_open(each).content
            f.write(img)
            file_name += 1

if __name__ == '__main__':
    global filename
    os.mkdir("image34")
    os.chdir("image34")
    file_name = 1
    url = 'http://www.mzitu.com/mm/'
    adds = get_page(url)
    get_image_adds(adds)


