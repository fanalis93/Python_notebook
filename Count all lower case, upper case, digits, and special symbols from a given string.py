str1 = "P@#yn26at^&i5ve"
chars=0
digits=0
symbol=0
for c in str1:
    if c.islower() or c.isupper():
        chars += 1
    elif c.isnumeric():
        digits += 1
    else:
        symbol += 1
print('chars = ',chars,'\ndigits = ',digits,'\nsymbol = ',symbol)