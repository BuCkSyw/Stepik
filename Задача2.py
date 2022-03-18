n=int(input())
scopes = {'global': {'parent': None, 'variables': set()}}
def add(pr,x):
    scopes[pr]['variables'].add(x)
def create(pr,ppr):
    scopes[ppr]={'parent': pr, 'variables':set()}
def get(pr,x):
    while scopes[pr]['parent']!= None:
        if x in scopes[pr]['variables']:
            return print(pr)
        else:
            pr=scopes[pr]['parent']
    if x in scopes[pr]['variables']:
        return print(pr)
    else:
        print('None')
for i in range(n):
    s=input().split()
    if s[0]=='create':
        create(s[2],s[1])
    elif s[0]=='add':
        add(s[1],s[2])
    elif s[0]=='get':
        get(s[1],s[2])