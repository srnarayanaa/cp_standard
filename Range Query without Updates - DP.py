# cook your dish here
#srnarayanaa
#range query without updates - DP
def findSum(DP, L, R):
    range_sum=DP[R]-DP[L-1]
    return int(range_sum)
def preprocess(arr, N):
    DP=[0]*(N+1)
    for i in range(1,N+1):
        DP[i]=DP[i-1]+arr[i-1]
    return DP
    
N, Q=map(int,input().split())
arr=list(map(int,input().split()))
DP=preprocess(arr, N)
for _ in range(Q):
    L, R = map(int, input().split())
    print(findSum(DP, L, R))
    
