if __name__ == '__main__':
    lis = []
    N = int(input())
    for i in range(N):
        cmd = input()
        if " " in cmd :
            cmd_lis = cmd.split(" ")
            if cmd_lis[0] == 'insert' :
                lis.insert(int(cmd_lis[1]),int(cmd_lis[2]))
            elif cmd_lis[0] == 'remove' :
                lis.remove(int(cmd_lis[1]))
            else :
                lis.append(int(cmd_lis[1]))
        else :
            if cmd == 'print' :
                print(lis)
            elif cmd == 'sort' :
                lis.sort()
            elif cmd == 'pop' :
                lis.pop()
            else :
                lis.reverse()