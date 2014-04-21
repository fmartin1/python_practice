number = 2
candidate = 0
goal = 600851475143

def isprime(n):
    if not n & 1: return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0: return False
    return True


while number < goal:
    if goal % number == 0: 
        candidate = goal / number;
        if isprime(candidate): print candidate; break
    number += 1