def f(x):
    return 2*x**2 - 12*x + 7
    
def maximize(a, b):
    (left, right) = (a, b)
    while left - right >= 3:
      left_third = ((2 * left) + right) / 3
      right_third = (left + (2 * right)) / 3
 
      if func(left_third) < func(right_third):
            right = right_third
      else:
            left = left_third
    if (left == right):
      return f(left)
    elif (left + 1 == right):
      return min(f(left), f(right))
    else:
      return min(f(left), min(f(left+1), f(left+2)))

for _ in range(int(input())):
  A = sorted(map(int, raw_input().split()))
  print maximize(A.pop(0), A.pop(0))
 
