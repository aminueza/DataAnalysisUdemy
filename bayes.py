# Write your code here
p1=float(input())
p2=float(input())
p3=int(input())
if p3>=2:
#P(X) = P(X ∩ Y) + P(X ∩ Y')
    print("%.6f" % (p2*(1-p1) + p1*2/p3))
