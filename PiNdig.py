from math import pi
x = str(pi)
y = input("What decimal point to?")
i = 0
output = "3."
while i < y:
    output = output+x[i+2]
    i += 1
print(output)
