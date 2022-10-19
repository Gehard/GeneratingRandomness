numbers = input()
n = input()

x = numbers.split()

if n not in x:
    print("not found")

else:
    indices = [index for index, element in enumerate(x) if element == n]
    str1 = ' '.join(str(e) for e in indices)
    print(str1)
