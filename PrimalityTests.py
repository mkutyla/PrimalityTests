import random as rand
import math
import time


'''
This function is an implementation of Miller-Rabin primality test.

Parameters:
n- number to be tested (positive odd integer greater than 2)
k- number of tests to run on number n (positive integer)

Returns:
false, if number is determined to be composite
true, otherwise

Probability that a composite number n passes k tests is (1/4)^k
'''
def MillerRabin (n, k=30):

    # Catching wrong input
    if n <= 3:
        return n == 2 or n==3
    if n % 2 == 0:
        return False
    
    # Finding d and r such that: n-1 = d * 2^s 
    d = n-1
    s = 0
    while(d%2 == 0):
        d //=2
        s+=1

    # Running k tests
    for i in range(k):
        a = rand.randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        
        witness = True
        for r in range(s): 
            x = (x*x)%n
            if x == n-1:
                witness = False
                break
        if(witness):
            return False
    return True

'''
This function is an implementation of Fermat primality test.

Parameters:
n- number to be tested (positive odd integer greater than 3)
k- number of tests to run on number n (positive integer)

Returns:
false, if n is determined to be composite
true, otherwise
'''
def Fermat(n, k=30):
    if n<4:
        return n==2 or n==3
    for i in range(k):
        a = rand.randint(2, n-2)
        while math.gcd(a,n)!=1:
            a = rand.randint(2, n-1)
        if pow(a, n-1, n) != 1:
            return False
    return True


'''
This function is a primality test based on the Sieve of Erathosthenes.
It is improved by taking only int(math.sqrt(n)) + 1 memory space with the array
This also implies checking whether a prime divides n rather than running through the entire array
and check if array[n] stores 'True' at the end.

Parameters:
n- number to be tested (positive integer)

Returns:
false, if n is composite
true, if n is prime
'''
def Erathosthenes(n):
    bound = int(math.sqrt(n)) + 1
    array = [True for i in range(bound)]

    for i in range(2, bound):
        if array[i]:
            if n % i ==0:
                return False
            for j in range(i*i, bound, i):
                array[j] = False
    return True


if __name__ == '__main__':
        numbers = [548206114665289, 714260116691963, 318690492236731, 292698299205553, 861865351443589,
        43278627594613, 35864511406127, 35484763727641, 39053643531401, 43897136579389]

        file = open("results.txt", "w")

        results = []
        file.write("Miller-Rabin primality test\n")
        start = time.time()
        for number in numbers:
            results.append(MillerRabin(number))
        file.write("Execution time: {}\n".format(time.time()-start))
        file.write("Results: {}\n".format(results))

        results = []
        file.write("Fermat primality test\n")
        
        start = time.time()
        for number in numbers:
            results.append(Fermat(number))
        file.write("Execution time: {}\n".format(time.time()-start))
        file.write("Results: {}\n".format(results))
        

        results = []
        file.write("Sieve of Erathosthenes\n")
        start = time.time()
        for number in numbers:
            results.append(Erathosthenes(number))
        file.write("Execution time: {}\n".format(time.time()-start))
        file.write("Results: {}\n".format(results))

        print("Executed")
