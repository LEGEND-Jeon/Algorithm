#백준25972번

n= int(input())
lis=[]
cnt=1
for i in range(n):
  lis.append(list(map(int,input().split())))


for i in range(1,n):
  if (lis[i-1][0]+lis[i-1][1]) >= lis[i][0]: 
    continue
  else:
    cnt+=1
print(cnt)
