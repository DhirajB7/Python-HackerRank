n,m = map(lambda a:int(a),input().split(' '))
for i in range(1,n,2) :
    print(('.|.'*i).center(m,'-'))
print('WELCOME'.center(m,'-'))
for i in range(1,n,2) :
    print(('.|.'*(n-1-i)).center(m,'-'))