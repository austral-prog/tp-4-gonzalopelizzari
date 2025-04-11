import math

def line():
    def calcular_y(a,b,x):
        return a*x+b
    def calcular_distancia(x1,y1,x2,y2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    a= float(input("Ingrese el coeficiente A: "))
    b= float(input("Ingrese el coeficiente B: "))
    x1= float(input("Ingrese el valor de X1: "))
    x2= float(input("Ingrese el valor de X2: "))

    print(f"El coeficiente A de su ecuación de la recta es: {a}")
    print(f"El coeficiente B de su ecuación de la recta es: {b}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {x2}")

    y1= a * x1  +  b
    y2= a * x2  +  b
   
    print(f"\nPara la siguiente ecuación:\n\tY = {a}X + {b}")

    print("\nDados los siguientes puntos:")
    print(f"\tP1 ({x1}, {y1})")
    print(f"\tP2 ({x2}, {y2})")
    if(x2>x1):
        distancia= math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    else:
        distancia= math.sqrt(((x1-x2)**2)+((y1-y2)**2))


   
    print(f"\nLa distancia entre ellos es: {distancia}")
