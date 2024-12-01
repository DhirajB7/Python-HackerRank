a = int(input())
lis = []
mp = {}

for x in range(0,a) :
    lis.append(input())

for x in lis :
    if x in mp :
        mp[x] = mp.get(x) + 1
    else:
        mp[x] = 1


print(len(set(lis)))
print(" ".join(list(map(lambda y:str(y),list(mp.values())))))

