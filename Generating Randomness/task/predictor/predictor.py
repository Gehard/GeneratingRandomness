final_string = ''
while len(final_string) < 100:
    input_string = input("Print a random string containing 0 or 1:\n\n")
    final_string += ''.join(i for i in input_string if i in '01')
    print(f"Current data length is {len(final_string)}"
          f", {100 - len(final_string)} symbols left")
print(f"\nFinal data string:\n{final_string}")
triads = ['000', '001', '010', '011', '100', '101', '110', '111']
parts = [final_string[index:index + 4] for index in range(0, len(final_string) - 3)]
for x in triads:
    res_0 = parts.count(x + '0')
    res_1 = parts.count(x + '1')
    print(f'{x}: {res_0}, {res_1}')