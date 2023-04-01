#백준 16924번

n,m=map(int,input().split())
cnt=0
an=[]
lis=[list(map(str,input())) for i in range(n)]

for i in range(1,n):
  for j in range(1,m):
    z=min(i,j)
    for k in range(1,z+1):
      if j+k==m:
        break
      if lis[i][j]=='*'==lis[i][j+k]==lis[i][j-k]==lis[i+k][j]==lis[i-k][j]:
        cnt+=1
        an.append([i+1,j+1,k])
if cnt==0:
  print(-1)
else:
  print(cnt)
  for i in range(cnt):
    for j in range(cnt):
      print(an[i][j],end=' ')
    print()
