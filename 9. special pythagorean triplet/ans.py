c = 0
for a in range(3, 998):
    for b in range(3, 1000-a):
        if a**2 + b**2 == (1000 - a - b)**2:
            print(a*b*(1000 - a - b))
            c = 1
            break
    if c:
        break