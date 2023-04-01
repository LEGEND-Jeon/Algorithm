#백준 1697번

n,k=map(int,input().split())

q=[n]
visit=[0]*10000
x=n
while q:
    if x==k: #x:현재위치
        print(visit[x]) 
        break
    x= q.pop(0)
    for i in(x-1,x+1, 2*x):
        if not visit[i]:
            visit[i]=visit[x]+1 
            q.append(i)
