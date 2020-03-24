s=open("/etc/passwd","r").readlines()
l=len(s)-1
while l > 0:
    l=l-1
    print(s[l])

