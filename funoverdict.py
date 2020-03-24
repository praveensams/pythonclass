def add(**k):
    r=0
    for i in  k.keys():
        r=k[i]+r
    return r

j=add(a=10,b=30)
print(j)
