prime_list = set()
prime_list.add(1)
prime_list.add(2)
prime_list.add(3)
def factorsof(number):
    div = number
    last_factor = 1
    # First factor
    factors = set()
    factors.add(1)
    factors.add(number)
    
    while True:
        # Get the next factor that can divide the number
        if div == number: 
            p = nextDividend(div,last_factor + 1)
            last_factor = p
        else: p = nextDividend(div,2)
        if p == 0: break
        
        factors.add(p)
        div = div / p
        factors.add(div)
        if prime(div):
            div = number
    print number,"\t", len(factors), factors
    return len(factors)
            
def nextDividend(number,last):
    for x in range(last, number):
        if number % x == 0:
            return x
    return 0

def triangleNum(x):
    return (x * (x+1) ) / 2

def prime(n):
    if n in prime_list: return True
    
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    prime_list.add(n)
    return True
    
    
nat_num = 5
facs = 0
while facs <= 5:
    facs = factorsof( triangleNum(nat_num) )
    nat_num += 1
print factorsof(2162160)