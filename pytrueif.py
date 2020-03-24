import sys
try:
    s=int(sys.argv[1])
except:
    pass

if s%2 == 0:
    d=True
else:
    d=False

if d:
    print("It is even number")
