def bubbleSort(alist):
    v = 0
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                v += 1
    return v
                
N = int(input())              
A = map(int, raw_input().split())

print bubbleSort(A)
