# List of know prime factors
pfs = []
f = open("euler012_primes.txt")

def fillPrimes():
    with open('euler012_primes.txt') as f:
        for line in f:
            pfs.append( int(line) )
    f.close
    print "Primes loaded."

def factorize(num):
    facs = set()
    facs.add(1)
    facs.add(num)
    usedP = set()
    
    curr = num
    curf = 1
    
    while True:
        if curr == num:
            curf = nextPrime(curf)
            if num % curf: break
            if curf in usedP: continue
        else:
            curf = nextPrime(curf)
        if curr % curf == 0:
            facs.add(curf)
            if curr == num: usedP.add(curf)
            curr = curr / curf
            facs.add(curr)
            curf = 1
        if curr in pfs:
            curr = num
    print len(facs)
    
        
def nextPrime(x):
    return pfs[ pfs.index(x) + 1 ]
def nextDividend(x):
    
def nextMinPrime(x):
    p = 1
    while nextPrime(p) in x:
        p = nextPrime(x)
    return p
    
fillPrimes()
#factorize(2162160)
factorize(28)