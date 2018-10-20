def findpo(plist,temp):
    flag = 0
    list_index = []
    for n in range(plist.count(temp)):
        sec = flag
        flag = plist[flag:].index(temp)
        list_index.append(flag + sec)
        flag = list_index[-1:][0] + 1
    return list_index
c=[1,2,3,4,4,4,4,3,2,0,1]
print (findpo(c,max(c))
