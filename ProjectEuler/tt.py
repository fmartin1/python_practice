x = 28
p = 3
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
def nextPrime(x):
    x += 1
    while not prime(x):
        x += 1
    return x    

    

while x % p != 0 and p < x:
    p = nextPrime(p)
print p