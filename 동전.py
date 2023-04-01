#백준 11047번

N, K=map(int, input().split())
price=[]
for i in range(N):
  a=int(input())
  price.append(a)
price.sort(reverse=True) #큰거부터 오게 .sort(reverse=True)
cnt=0
for i in range(N): #4200=1000*4+100*2 -> 6
  while(1):
    if (K-price[i])>=0:
      K-=price[i]
      cnt+=1
    else:
      break
print(cnt)
