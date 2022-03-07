# Burnside transition matrix

import random
import itertools
import collections
import numpy as np
import math

#initialize parameters (n >= k)

# jx = number of distinct parts of set partition x
# jy = number of distinct parts of set partition y

def factorial(j):
    if j<0:
        return 0
    else:
        return np.math.factorial(j)

def subfactorial(j):
    sum = 0
    s = 0
    for i in range(0,j+1):
        sum += (pow(-1, i))/(float(factorial(i)))
    s = factorial(j)*sum
    return(s)
def stirling(n,k):
    n1=n
    k1=k
    if n<=0:
        return 1
     
    elif k<=0:
        return 0
     
    elif (n==0 and k==0):
        return -1
     
    elif n!=0 and n==k:
        return 1
     
    elif n<k:
        return 0
 
    else:
        temp1=stirling(n1-1,k1)
        temp1=k1*temp1
        return (k1*(stirling(n1-1,k1)))+stirling(n1-1,k1-1)

def innerprob(j,k,n):
    sum = 0
    for i in range(0,n-j+1):
        sum += (1/float(pow(j+i, k)*factorial(i)))*(subfactorial(n-j-i)/(factorial(n-j-i)))
    return sum

def transitionQ(jx, jy, k, n):
    sum = 0
    c = 0
    d = 0
    e = 0
    f = 0
    for j in range(jy, jx+jy+1):
        c = (factorial(jx)*factorial(jy))
        d = (factorial(j-jx)*factorial(j-jy)*factorial(jx+jy-j))
        e = innerprob(j,k,n)
        f = (float(c)/float(d))*e
        sum = sum + f
    return(sum)

def Q(i, j, k, n):
    if i <= j:
        return transitionQ(i, j, k, n)
    else:
        return transitionQ(j, i, k, n)


# for n in range(k*k,k*k+1):
#     print(n)
#     for i in range (1, k+1):
#         for j in range(1,k+1):
#             print(stirling(k,j)*Q(i, j, k, n))
#         print '\n'
#     print '\n'

# k = 8
# n = k*k
# print(n)
# for i in range (1, k+1):
#     for j in range(1,k+1):
#         print(stirling(k,j)*Q(i, j, k, n))
#     print '\n'
# print '\n'

# without stirling
k=8
n=k*k
print('k = ', k)
print('n= ', n)
print '\n'
for i in range (1, k+1):
    print(i)
    for j in range(1,k+1):
        print(Q(i, j, k, n))
    print '\n'
print '\n'


