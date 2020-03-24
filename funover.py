def overloads(a,*b):
    y=0
    for i in b:
        y=i+y
    print(y)

overloads(1,2,3,4,5,6,7)
