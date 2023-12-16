# Write a Python code to input the lengths of the three sides of a triangle and display whether a triangle can be formed with the inputs or not. If a triangle can be formed then displaý whether the triangle will be scalene, isosceles or equilateral triangle.

def triangle(a,b,c):
    if (a + b) > c and (b + c) > a and (a + c) > b:
        if a == b == c:
            return "Se puede formar un triangulo. Es un triangulo equilatero"
        elif a != b and b != c and c != a:
            return "Se puede formar un triangulo. Es un triangulo escaleno"
        else:
            return "Se puede formar un triangulo. Es un triangulo isosceles"
    else:
        return "No se puede formar un triangulo."
    
a = float(input("input enter a"))
b = float(input("input enter b"))
c = float(input("input enter c"))

print(triangle(a,b,c))