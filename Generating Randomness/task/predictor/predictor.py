final_string = ''
while len(final_string) < 100:
    input_string = input("Print a random string containing 0 or 1:\n\n")
    final_string += ''.join(i for i in input_string if i in '01')
    print(f"Current data length is {len(final_string)}"
          f", {100 - len(final_string)} symbols left")
print(f"\nFinal data string:\n{final_string}")