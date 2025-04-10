def line():
    def calcular_y(a,b,x):
        return a*x+b
    def calcular_distancia(x1,y1,x2,y2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    a= float(input("Ingrese el coeficiente A: "))
    b= float(input("Ingrese el coeficiente B: "))
    x1= float(input("Ingrese el valor de X1: "))
    x2= float(input("Ingrese el valor de X2: "))

    print(f"\nEl coeficiente A de su ecuacion de la recta es: {a}")
    print(f"El coeficiente  B de su ecuacion de la recta es: {b}")
    print(f"El coeficiente X1 de su ecuacion de la recta es: {x1}")
    print(f"El coeficiente de X2 de su ecuacion de la recta es: {x2}")

    y1= calcular_y(a,b,x1)
    y2=calcular_y(a,b,x2)
   
    print(f"\nPara la siguiente ecuacion:\nY = {a}X+{B}")

    print("\nDados los siguientes puntos:")
    print(f"P1 ({x1} , {y1})")
    print(f"P2 ({x2} , {y2})")

    distancia = calcular_distancia(x1, y1, x2, y2)
    print(f"\nLa distancia entre ellos es: {distancia}")
    line()
