#백준 3986번
n=int(input())
lis = [list(map(str, input())) for i in range(n)] #문자열 2차원 리스트로 input 받기
stack=[]
cnt=0
answer=0
#stack에 맨 뒤 리스트 append -> stack 맨 뒤랑 리스트 맨 뒤 비교 -> 같으면 remove
for i in range(n):
  stack.append(lis[i][-1])
  lis[i].pop()
  for j in reversed(range(len(lis[i]))): #뒤에서부터 for문 돌기
    if stack[-1]==lis[i][-1]:
      stack.pop()
      lis[i].pop()
    elif stack[-1]!=lis[i][-1]:
      stack.append(lis[i][-1])
      lis[i].pop()
    if not lis[i]:
      break
    if not stack:
      stack.append(lis[i][-1])
  if not stack:
    answer+=1
print(answer)
