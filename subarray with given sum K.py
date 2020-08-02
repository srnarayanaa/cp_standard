#cook your dish here
#srnarayanaa
#subarray with given sum K
N,K=map(int,input().split())
arr=list(map(int,input().split()))
curr=0
d={}
for i in range(N):
    curr+=arr[i]
    if curr not in d:d[curr]=i
    if K==curr:
        ans=[0,i]
        break
    if curr-K in d:
        ans=[i,d[curr-K]+1]
        break 
    
print(' '.join(str(i+1) for i in sorted(ans)))
    
