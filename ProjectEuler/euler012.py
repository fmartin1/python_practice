import math
max_value = 999999999999999999999999999999
num_of_divisors = 200
tri_num = 28
nat_num = 3
x = 0

def divisorsof(x):
    result = 1
    list = []
    for divisor in range( 2, x ):
        if x % divisor == 0: 
            result += 1
            if prime(divisor): list.append(divisor)
    print x,result,"\tdivisors in total","prime divisors",list
    return result

def triangleNum(x):
    return (x * (x+1) ) / 2

def prime(x):
    x = abs(int(x))
    # 0 and 1 are not primes
    if x < 2:
        return False
    # 2 is the only even prime number
    if x == 2: 
        return True    
    # all other even numbers are not primes
    if not x & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for number in range(3, int(x**0.5)+1, 2):
        if x % number == 0:
            return False
    return True
    
for i in range(1,200):
    divisorsof(i)
