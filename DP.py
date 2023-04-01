#백준 11053

score=[]
lis1=[]
lis=[]
N, M=map(int,input().split())
for i in range(0,N):
    lis1.append(str(input()))
cnt=0
for k in range(0,M):
    lis2=list(map(str,input().split(',')))
    N=N-cnt
    cnt=0
    for i in range(0,M):
        for j in range(0,len(lis2)):
            if lis1[i]==lis2[j]:
                lis1.pop(i)
                cnt=cnt+1
    lis.append(N-cnt)        

for i in lis:
    print(i)
