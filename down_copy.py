import requests
import os
import re

#获取网页信息
def url_open(url):
  #添加头部信息记得加上 Referer,不然图片地址会变成防盗链接
  headers = {'User-Agent':
             'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
             ,"Referer":"http://www.mzitu.com/"}
    
  response = requests.get(url, headers=headers)
  return response

#得到所有网址套图的地址
def get_page(url):
  phtml = url_open(url).text
  #print(phtml)
#正则匹配套图地址
  page_p = r'<a href="([^"]+\d+)" target="_blank">'
  page_addrs = []
  #for 循环去除正则匹配的重复图片套图地址有
  for i in re.findall(page_p,phtml):
    if i in page_addrs:
      continue
    else:
      page_addrs.append(i)
  return page_addrs
  #print(page_addrs)
 
#把每个网页套图里的所有图片下载保存到文件夹中
def get_img(url):
  os.mkdir("MeiZiTu")
  os.chdir("MeiZiTu")
  
  page_addrs = get_page(url)
  print(page_addrs)
  for  page_url in page_addrs:
    print(page_url)
    img_html1 = url_open(page_url).text
    #print(ihtml)
    #正则匹配套图页数
    p = r'<span>(\d+)</span>'
    p_url = re.findall(p,img_html1)
    #print(p_u)
    #取套图的最大页数
    x = int(p_url[-1])
    #print(x)
    
    for i in range(1,x+1):
      img_url = page_url + "/" + str(i)
      #print(img_url)
      img_html2 = url_open(img_url).text
      #print(img_html2)
      #匹配图片地址
      img_p = r'<img src="([^"]+\.jpg)"'
      img_addrs =  re.findall(img_p,img_html2)
      
      for each in img_addrs:
        #print(each)
        file = each.split("/")[-1]
        with open(file, "wb") as f:
          img = url_open(each).content
          f.write(img)
      

if __name__ == "__main__":
  url = 'http://www.mzitu.com/'
  get_img(url)
