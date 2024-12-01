lis = list(input())
lis.sort()
dict_frq = {}
for x in lis :
    if x in dict_frq :
        dict_frq[x] = dict_frq[x] + 1
    else :
        dict_frq[x] = 1
dict_other = sorted(dict_frq.items(), key=lambda a: a[1], reverse=True)
for x in range(0,3):
    print(dict_other[x][0],dict_other[x][1])