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
            p = nextDividend(div,last_factor+1)
            last_factor = p
        else:
            p = nextDividend(div,2)
        if p == 0:
            break
        
        factors.add(p)
        div = div / p
        factors.add(div)
        if nextDividend(div,2) == 0:
            p = 1
            div = number
    return len(factors)
            
def nextDividend(number,last):
    for x in range(last, number):
        if number % x == 0:
            return x
    return 0

def triangleNum(x):
    return (x * (x+1) ) / 2


nat_num = 1150
facs = 0
while facs <= 500:
    facs = factorsof( triangleNum(nat_num) )
    nat_num += 1
    print facs,"\t",nat_num