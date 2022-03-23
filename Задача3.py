d={}
n=int(input())
for i in range(n):
    s=input().split()
    if len(s)<2:
        d[s[0]]=[]
    else:
        for j in range(2,len(s)):
            if s[0] in d:
                d[s[0]].append(s[j])
            else:
                d[s[0]]=list()
                d[s[0]].append(s[2])
for key, value in d.items():
    for key2, value2 in d.items():
        for m in range(len(value2)):
            if value2[m] == key:
                for l in range(len(value)):
                    value2.append(value[l])
q=int(input())
for i in range(q):
    s=input().split()
    if len(s)==1:
        if d.get(s[0])!=None and d.get(s[0])!=[]:
            print('Yes')
        else:
            print('No')
    elif s[1] == s[0]:
            print('Yes')
    else:
        for j in range(len(d.get(s[1]))):
            if s[0] == d.get(s[1])[j]:
                print('Yes')
                break
        else:
            print('No')