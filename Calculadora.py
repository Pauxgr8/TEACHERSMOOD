def mostrar_resultado(resultado):
    print("-------------------------------------")
    print("| El resultado de la operación es: " + str(resultado) + " |")
    print("-------------------------------------")


def menu():
    print("/********************************************/")
    print("/ Calculadora                                /")
    print("/                                            /")
    print("/ 1- Suma                                    /")
    print("/ 2- Resta                                   /")
    print("/ 3- Multiplicación                          /")
    print("/ 4- División                                /")
    print("/ 5- Salir                                   /")
    print("/                                            /")
    print("/********************************************/")
    seleccion = input("¿Qué quieres resolver: ")
    return seleccion


operacion_a_realizar = menu()

while operacion_a_realizar != '5':
    numero1 = input("Ingrese el primer número: ")
    numero2 = input("Ingrese el segundo número: ")

    if operacion_a_realizar == "1":
        suma = int(numero1) + int(numero2)
        mostrar_resultado(suma)
    elif operacion_a_realizar == "2":
        resta = int(numero1) - int(numero2)
        mostrar_resultado(resta)
    elif operacion_a_realizar == "3":
        multiplicacion = int(numero1) * int(numero2)
        mostrar_resultado(multiplicacion)
    elif operacion_a_realizar == "4":
        division = int(numero1) / int(numero2)
        mostrar_resultado(division)
    else:
        print("*************************************")
        print("* Ha ingresado un dígito incorrecto *")
        print("*************************************")

    operacion_a_realizar = menu()

print("Usted ha elegido salir")