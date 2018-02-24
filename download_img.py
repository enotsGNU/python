from test1 import *
import json

def get_image_adds(page_adds):
    file_name = 1
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
        print('在下载哦')
        download(img_adds)
        #下载一套图
                 
def download(img_adds):
    file_name =1
    for each in img_adds:
        with open(str(file_name)+'.jpg',"wb") as f:
            img = url_open(each).content
            f.write(img)
            file_name += 1
if __name__ == '__main__':
    with open('jsdate','r')as f:
        js = json.load(f)
    os.mkdir("image13")
    os.chdir("image13")
    for i in js:
        get_image_adds(i)
