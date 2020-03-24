def oddeven(name):
    if name%2 == 0:
        return True
    else:
        return False

if oddeven(10):
    print("Given number is Even")

def addsub(a,b):
    return a+b,a-b

add,sub=addsub(20,10)

y="Addd   " + str(add) + "\n" + "Subb  " + str(sub)
print(y)
