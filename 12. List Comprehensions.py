if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    lis = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    answer=[]
    for i,j,k in lis :
        if i+j+k!=n :
            answer.append([i,j,k])
    print(answer)