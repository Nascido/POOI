read = input()
abc = []
abc = read.split(" ")
a, b, c = abc

a = float(a)
b = float(b)
c = float(c)

delta = b**2 - 4*a*c

if delta < 0 or a == 0:
    print("Impossivel calcular")

elif delta == 0:
    x = round(-b/(2*a), 5)
    print(f"R1 = {x}")
    print(f"R2 = {x}")

else:
    x1 = round((-b + delta**0.5)/(2*a), 5)
    x2 = round((-b - delta**0.5)/(2*a), 5)

    print(f"R1 = {x1}")
    print(f"R2 = {x2}")
