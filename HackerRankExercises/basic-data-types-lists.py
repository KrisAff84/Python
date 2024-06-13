if __name__ == '__main__':
    N = int(input())
    mylist = []
    for i in range(N):
        spl = list(input().split())
        if spl[0] == 'insert':
            mylist.insert(int(spl[1]), int(spl[2]))
        if spl[0] == 'remove':
            mylist.remove(int(spl[1]))
        if spl[0] == 'append':
            mylist.append(int(spl[1]))
        if spl[0] == 'sort':
            mylist.sort()
        if spl[0] == 'pop':
            mylist.pop()
        if spl[0] == 'reverse':
            mylist.reverse()
        if spl[0] == 'print':
            print(mylist)
