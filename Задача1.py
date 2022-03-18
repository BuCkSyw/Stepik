n=int(input())
a=[[0 for j in range(n)] for i in range(n)]
d=0
i=0
j=0
s=1
while s<n*n:
  for j in range(d,n-1-d):
    a[i][j]=s
    s+=1
    j+=1
  for i in range(d,n-1-d):
    a[i][j]=s
    s+=1
    i+=1
  for j in range(n-1-d,d,-1):
    a[i][j]=s
    s+=1
    j-=1
  for i in range(n-1-d,d,-1):
    a[i][j]=s
    s+=1
    i-=1
  d+=1
  j+=1
  i+=1
if n%2==1:
  for i in range(n):
    for j in range(n):
      if a[i][j]==0:
        a[i][j]=s
for i in range(n):
    for j in range(n):
      print(a[i][j],end=' ')
    print()