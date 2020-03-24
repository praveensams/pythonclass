from sys import argv

d={}

for i in range(1,len(argv)):
    if argv[i] in d:
        y=d[argv[i]]
        d.update({argv[i]:y+1})
    else:    
        d.update({argv[i]:1})

print(d)
