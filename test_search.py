import pickle
import jieba
titledic={}
bodydic={}
with open("titleindex.pickle","rb") as f:
    titledic=pickle.load(f)
with open("bodyindex.pickle","rb") as f1:
    bodydic=pickle.load(f1)


search=input("input: ")
while search!="-1":
    word_list=jieba.cut_for_search(search)
    seg_list=jieba.lcut_for_search(search)
    print(seg_list)
    found_title=True
    found_body=True
    
    try:
        l1=titledic[seg_list[0]]
    except:
        found_title=False
    try:
        l2=bodydic[seg_list[0]]
    except:
        found_body=False
    """if seg_list[0] in titledic:
        l1=titledic[seg_list[0]]
        found_title=True
    if seg_list[0] in bodydic:
        l2=bodydic[seg_list[0]]
        found_body=True"""
    #print(l1)
    for i in word_list:
        #print(titledic[i])
            try:
                l1=list(set(l1).intersection(titledic[i]))
            except:
                found_title=False
            try:
                l2=list(set(l2).intersection(bodydic[i]))
            except:
                found_body=False

        #print(l1)
    if found_title:
        print(l1)
    pause=input("pause")
    if found_body:
        print(l2)
#    if search in titledic:
#        print(titledic[search])
#    else:
#        print("title not found")
#    print("\n\n\n")

    #if search in bodydic:
    #    print(bodydic[search])
    #else:
    #    print("body not found")
    search=input("input: ")

