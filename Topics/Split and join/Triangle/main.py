n = abs(int(input()))
for i in range(1, (n * 2), 2):
    x = []
    z = ''
    y = z.center(i, '#')
    j = y.center(n * 2)
    x.append(j)
    print(" ".join(x))
