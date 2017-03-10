import urllib.request
import re
import urllib
from multiprocessing import Pool
from bs4 import BeautifulSoup
import jieba
import pickle
readfile=open("result")
#outfile=open("title","w")
#outfile2=open("body","w")
#outfile3=open("fenci","w")
#outfile4=open("titleindex","w")
dic={}
dic2={}



while 1:
    #pool=Pool(4)
    url=readfile.readline()
    if not url:
        break
    try:
        urlop=urllib.request.urlopen(url)
    except:
        continue
    data=urlop.read().decode("gbk","ignore")
    linkre=re.compile("<title>.*?</title>")
    for x in linkre.findall(data):
        s=set()
        #y=unicode(x,'utf-8')
        index=x.find("_")
        y=x[7:index]
        #outfile.write(url)
        seg_list=jieba.cut_for_search(y)
        for i in seg_list:
            if i in dic:
                if i not in s:
                    dic[i].append(url)
                    s|={i}
            else:
                l1=[]
                dic[i]=l1
                dic[i].append(url)
        #outfile.write(" ".join(seg_list))
        #outfile.write("\n")
    linkre2=re.compile("id=\"content\">.*?<div class",re.S)
    for x in linkre2.findall(data):
        linkre3=re.compile("<.*?>",re.S)
        y=x[13:len(x)-10]
        for x1 in linkre3.findall(y):
            y=y.replace(x1," ")
        #y=y.replace("<br />"," ")
        y=y.replace("&hellip;","...")
        y=y.replace("&nbsp;","")
        y=y.replace("&ldquo;","\"")
        y=y.replace("&rdquo;","\"")
        y=y.replace("&mdash;","-")
        y=y.replace("&middot;","")
        seg_list=jieba.cut_for_search(y)
        s=set()
        for i in seg_list:
            if i in dic2:
                if i not in s:
                    dic2[i].append(url)
                    s|={i}
            else:
                l1=[]
                dic2[i]=l1
                dic2[i].append(url)



        #outfile3.write(url)
        #outfile3.write(" ".join(seg_list))
        #outfile3.write("\n\n")
        #y=y.replace("<strong>","")
        #y=y.replace("<\strong>","")
        #outfile2.write(url)
        #outfile2.write(y)
        #outfile2.write("\n")
#outfile4.write(str(dic))
#outfile2.close()
#outfile3.close()
#outfile4.close()
with open("titleindex.pickle","wb") as f:
    pickle.dump(dic,f)
with open("bodyindex.pickle","wb") as f1:
    pickle.dump(dic2,f1)
"""soup=BeautifulSoup(data,"html.parser")
soup=soup.decode("gbk","ignore")
print(soup.get_text())"""
