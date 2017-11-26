#Probability that Alice will accidentally drop her phone to ground is p. 
#She will not be careful after any no.of unfortunate events. 
#Let X be the random variable that equals to the no.of times Alice drops her phone.

#Write a program to calculate the expectation value, E(X).

p=float(input())
if p>0 and p<1:
    print("%.6f" % (p/(1-p)**2))
