string = 'PyNaTive'
lower=[]
upper=[]
for c in string:
    if c.islower():
        lower.append(c)
    else:
        upper.append(c)
print(''.join(lower+upper))