#백준 1260번
N,M,v=map(int, input().split())

#dfs-재귀
def dfs(v):
  print(v, end=' ')
  global visit,s
  visit[v]=1
  for next in range(1, N+1):
    if visit[next]==0 and s[v][next]==1: #방문한적 없고 s는 1인
      dfs(next)
      
#bfs-q,cur
def bfs(v):
  global q,visit,s
  q=[v]
  visit[v]=1
  while q: #q가 있을때까지
    cur=q.pop(0) #cur: q 0번째 인덱스, q는 계속 줄어드는중..
    print(cur,end=' ')
    for next in range(1, N+1):
      if visit[next]==0 and s[cur][next]==1:
        visit[next]=1
        q.append(next)
      


s= [[0]*(N+1) for i in range(N+1)]
visit=[0]*(N+1)

for i in range(M):
  x,y=map(int,input().split())
  s[x][y]=s[y][x]=1

dfs(v)
print()


visit=[0]*(N+1)
bfs(v)
