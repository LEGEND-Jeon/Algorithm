#백준 2490번
lst = []
while True:
    nData = list(map(int, input().split()))
    lst.append(nData)
    if lst[-1] == []:
        lst.remove(lst[-1])
        print(lst)
        break
lis=[]
for i in lst:
    if i.count(0)==0:
        lis.append("D")
    elif i.count(0)==1:
        lis.append("A")
    elif i.count(0)==2:
        lis.append("B")
    else:
        lis.append("C")

print(lis)
