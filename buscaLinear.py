#input
N, M = map(int, raw_input().split())
A = map(int, raw_input().split())

temp = -1

for valor in range (0, N):
    if valor == M:
        #last index of number
        temp = len(A) - A[::-1].index(M)

print temp
