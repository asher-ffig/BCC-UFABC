x = float(input())
y = float(input())
z = float(input())
triangulo = ""

if x <= 0 or y <= 0 or z <=0:
    print("Isto nao forma um triangulo")
elif (x + y)<z or (x + z)<y or (y + z)<x:
    print("Isto nao forma um triangulo")

elif x == y and y == z:
    triangulo = ("Equilatero")
elif x == y or y == z or x == z:
    triangulo = ("Isosceles")
elif x != y and y != z and x != z:
    triangulo = ("Escaleno")
else:
    print("Algo deu errado")

print(triangulo)
