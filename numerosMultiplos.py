N = int(input())
A = map(int, raw_input().split())

for s in range(0, N):
  for i in range(1, A.pop(0)+1):
    if i%3 == 0 and i%5 == 0:
      print "FizzBuzz"
    elif i%3 == 0:
      print "Fizz"
    elif i%5 == 0:
      print "Buzz"
    else:
      print i
