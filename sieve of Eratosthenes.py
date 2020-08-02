# cook your dish here
#srnarayanaa
#sieve of eratosthenes
def sieve(N):
    primes=[True]*N 
    primes[0]=primes[1]=False
    for (i, isprime) in enumerate(primes):
        if isprime:
            yield i 
            for j in range(i*i, N, i):     
                primes[j] = False

N=int(input())
#N>=2
p=list(sieve(N))
print(p)
