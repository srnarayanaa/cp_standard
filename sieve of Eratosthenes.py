# cook your dish here
#srnarayanaa
#sieve of eratosthenes
def sieve(N):
    primes=[True]*N 
    primes[0]=primes[1]=False
    for (i, isprime) in enumerate(primes):
        #print(i,primes)
        if isprime:
            yield i 
            #instead of 2*i, i*i optimization -> this for loop makes all factors false
            for j in range(i*i, N, i):     
                primes[j] = False

N=int(input())
#N>=2
p=list(sieve(N))
print(p)
