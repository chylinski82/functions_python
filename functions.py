
import math

from numpy import Infinity

def  zeta_function(x, r=1000):
    result = 0
    i = 1
    while i < r:
        result += 1 / i ** x
        i += 1
    return result

def is_prime(x):
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True

def next_prime(x):
    while is_prime(x + 1) == False:
        x += 1

    return x + 1

def sum_of_primes(x):
    if x % 2 == 0:
        prime = 2
        while is_prime(x - prime) == False:
            prime = next_prime(prime)
        return prime, x - prime
    return 'enter an even number'

def twin_primes(x):
    if is_prime(x) == False:
        x = next_prime(x)
    twin  = next_prime(x)
    while twin - x != 2:
        x = twin
        twin = next_prime(x)
    return x, twin

def prime_factors(x):
    arr = []
    y = 1
    prime = 2
    while True:
        if is_prime(x):
            arr.append(x)
            return arr
        elif x % prime == 0:                 #checks if it can divide by current prime
            arr.append(prime)
            y = x / prime                        
            if is_prime(y):
                arr.append(y)
                return arr                  
            x = y                           #then it will check the same for the result of the division
        else:
            prime = next_prime(prime)       #if not it will do all the above for the next prime

def harmonic_series(x):
    result = 0
    i = 1
    while i <= x:
        result += 1/i
        i +=1
        print(result)
    return result


#print(zeta_function(-1, 1000000))

def egyptian_fractions(x):
    n = 2
    nn = 3
    y = x
    result = []
    written_result = []
    while True:
        if y >= 1/n:          
            result.append(1/n)
            written_result.append(['1 /', n])
            print('1 /', n)
            print(sum(result))
            print(result)
            y = y - 1/n
            if y == 0:
                return written_result
            print('y:', y)
            if x - sum(result) < 0.0001:
                result.clear()
                written_result.clear()
                n = nn
                nn += 1
                y = x
        else:
            n = n + 1

print(egyptian_fractions(0.15))
        

        


'''
num = 200000
below10k = 0
below20k = 0
below30k = 0
below40k = 0
below50k = 0
below60k = 0
below70k = 0
below80k = 0
below90k = 0
below100k = 0

while num < 300000:

    if num < 210000:
        below10k += 1
    elif num < 220000:
        below20k += 1
    elif num < 230000:
        below30k += 1
    elif num < 240000:
        below40k += 1
    elif num < 250000:
        below50k += 1
    elif num < 260000:
        below60k += 1
    elif num < 270000:
        below70k += 1
    elif num < 280000:
        below80k += 1
    elif num < 290000:
        below90k += 1
    else:
        below100k += 1
    
    num = twin_primes(num)[1]
    print(twin_primes(num), '\n', below10k, below20k, below30k, below40k, below50k, below60k, below70k, below80k, below90k, below100k, end='\r')

print(below10k, below20k, below30k, below40k, below50k, below60k, below70k, below80k, below90k, below100k)
'''    






'''
c = 1000
while c < 2000000:
    zeta_function(1 + 38j, c)
    c = c + 500000

imaginary = 25
while imaginary < 30:
    print(imaginary)
    zeta_function(1 + imaginary * 1j)
    imaginary += 0.5
'''