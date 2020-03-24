def sam(n):
    for i in range(0,n):
        yield i

d=sam(10)
print(d.next())
print(d.next())
print(d.next())
print(d.next())
print(d.next())
