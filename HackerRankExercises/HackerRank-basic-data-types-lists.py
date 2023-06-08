if __name__ == '__main__':
    N = int(input())
    mylist = [N]
    print(mylist)
    del mylist[0]
    mylist.append(N)
    mylist.sort()
    mylist.pop(-1)
    mylist.reverse()



