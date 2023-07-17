def mayor(a, b):
    if a > b:
        return a
    
    return b

a=434
b=43434
c=124
d=838

resultado1=mayor(a, b)

# resultado2=mayor(c, resultado1)
resultado2=mayor(c,d)

# resultado3=mayor(d, resultado2)
resultado3=mayor(resultado1, resultado2)

print(resultado3)