import numpy
import math


n=10
y = numpy.zeros((n))
a=0
b=math.pi/2
l=1
h=(b-a)/10
x=numpy.zeros((n))
def k(x,s):
    return(math.cos(s)*math.sin(x))

def f(x):
    return(1)
X = numpy.zeros((n))
X[0] = a + h 
for i in range(1,n):
    X[i] = X[i - 1] + h
sum = 0
y[0] = f(X[0])
y[1] = (f(X[1]) + (l * h * k(X[1], X[0])*y[0])/2)/(1- l * h * k(X[1], X[1]) / 2)
for i in range(2,n):
    sum = 0
    for j in range(i-1):
        sum += 2 * l * h * k(X[i], X[j]) * y[j];                  
    y[i] = (f(X[i]) + (l * h * k(X[i], X[0]) * y[0] + sum) / 2) / (1 - l * h * k(X[i], X[i]) / 2)
for i in range(n):
    x[i] = i + 1          
for i in range(n):
    print("Y" , x[i] , " = ",y[i])
    
            
