p1=float(input())
p2=float(input())
p3=float(input())
if p3>0 and p3<1:
    print("%.6f" % (p3*(p1*(1-p2)+(1-p1)*p2)))
