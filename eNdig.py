from math import expm1
x = str(expm1(1))
y = input("What decimal point to?")
i = 0
output = "2."
while i < y:
    output = output+x[i+2]
    i += 1
print(output)
