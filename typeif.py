import sys
s="pravene"
try:
    s=int(sys.argv[1])
except Exception as e:
    print("Please pass the integer: \n\t{0}".format(e))
finally:
    print("completing the functionality")
print("bye")

