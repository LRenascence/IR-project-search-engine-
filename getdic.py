import urllib.request
import re
import urllib
from collections import deque
dicqueue=deque()
html=".html"

dic=open("dic","w")

url='http://www.view.sdu.edu.cn/new/sdnews/'
for i in range(n):
    new_url=url+str(i+1)+html
    dic.write(new_url)
    dic.write("\n")
url='http://www.view.sdu.edu.cn/new/list.php?catid=66&page='
for i in range(6):
    new_url=url+str(i+1)+html
    dic.write(new_url)
    dic.write("\n")
url='http://www.view.sdu.edu.cn/new/news/'
for i in range(485):
    new_url=url+str(i+1)+html
    dic.write(new_url)
    dic.write("\n")
url='http://www.view.sdu.edu.cn/new/xszh/'
for i in range(135):
    new_url=url+str(i+1)+html
    dic.write(new_url)
    dic.write("\n")
url='http://www.view.sdu.edu.cn/new/gzxy/'
for i in range(493):
    new_url=url+str(i+1)+html
    dic.write(new_url)
    dic.write("\n")
url='http://www.view.sdu.edu.cn/new/hzjl/'
for i in range(85):
    new_url=url+str(i+1)+html
    dic.write(new_url)
    dic.write("\n")
url='http://www.view.sdu.edu.cn/new/picture/'
for i in range(4):
    new_url=url+str(i+1)+html
    dic.write(new_url)
    dic.write("\n")
url='http://www.view.sdu.edu.cn/new/sdrw/'
for i in range(28):
    new_url=url+str(i+1)+html
    dic.write(new_url)
    dic.write("\n")
url='http://www.view.sdu.edu.cn/new/ydpt/'
for i in range(3):
    new_url=url+str(i+1)+html
    dic.write(new_url)
    dic.write("\n")
url='http://www.view.sdu.edu.cn/new/sdzt/'
for i in range(5):
    new_url=url+str(i+1)+html
    dic.write(new_url)
    dic.write("\n")
url='http://www.view.sdu.edu.cn/new/list.php?catid=65&page='
for i in range(74):
    new_url=url+str(i+1)+html
    dic.write(new_url)
    dic.write("\n")
url='http://www.view.sdu.edu.cn/new/list.php?catid=67&page='
for i in range(31):
    new_url=url+str(i+1)+html
    dic.write(new_url)
    dic.write("\n")
url='http://www.view.sdu.edu.cn/new/xsyg/'
for i in range(42):
    new_url=url+str(i+1)+html
    dic.write(new_url)
    dic.write("\n")
url='http://www.view.sdu.edu.cn/new/zjsd/'
for i in range(35):
    new_url=url+str(i+1)+html
    dic.write(new_url)
    dic.write("\n")
url='http://www.view.sdu.edu.cn/new/gzss/'
for i in range(653):
    new_url=url+str(i+1)+html
    dic.write(new_url)
    dic.write("\n")
url='http://www.view.sdu.edu.cn/new/xydt/'
for i in range(13):
    new_url=url+str(i+1)+html
    dic.write(new_url)
    dic.write("\n")
url='http://www.view.sdu.edu.cn/new/xsyy/'
for i in range(10):
    new_url=url+str(i+1)+html
    dic.write(new_url)
    dic.write("\n")
url='http://www.view.sdu.edu.cn/new/ssgc/'
for i in range(126):
    new_url=url+str(i+1)+html
    dic.write(new_url)
    dic.write("\n")
url='http://www.view.sdu.edu.cn/new/world/'
for i in range(23):
    new_url=url+str(i+1)+html
    dic.write(new_url)
    dic.write("\n")
dic.close()
