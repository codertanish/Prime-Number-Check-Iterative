import math
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
def primeCheck(number):
    for p in primes:
        if number%p == 0 and number != p: 
            return False
    if number == 1:
        return False
    for i in range(47, math.floor(math.sqrt(number)+1), 2):
        for p in primes:
            if i%p == 0:
                continue
        e = number/i
        print(e)
        if e.is_integer() and i != number:
            return False
    if number not in primes:
        primes.append(number)
    return True
