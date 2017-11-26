# Write your code here
def binarysearch(sequence, value):
    lo, hi = 0, len(sequence)
    while lo <= hi:
        mid = (lo + hi) // 2
        if sequence[mid] < value:
            lo = mid + 1
        elif value < sequence[mid]:
            hi = mid - 1
        else:
            return mid + 1
    return -1


N = int(input())
A = sorted(map(int, raw_input().split()))

#input q and x
for _ in range (int(raw_input())):
  print binarysearch(A, int(raw_input()))
