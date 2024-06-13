if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    unique_scores = list(set(list(arr)))
    print(sorted(unique_scores)[-2])



 
