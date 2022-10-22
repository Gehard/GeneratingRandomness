# put your python code here
year = abs(int(input().strip()))
print("Leap" if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else "Ordinary")
