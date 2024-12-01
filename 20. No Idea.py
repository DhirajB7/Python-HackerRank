n,m = map(lambda a:int(a),input().split(' '))
lis = list(map(lambda a:int(a),input().split(' ')))
happy_set = set(map(lambda a:int(a),input().split(' ')))
sad_set = set(map(lambda a:int(a),input().split(' ')))
count = 0
for x in lis :
    if x in happy_set :
        count += 1
    if x in sad_set :
        count -=1
print(count)