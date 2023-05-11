import random
import os
from fractions import Fraction
from math import sqrt
opcion = 0
valor_pendiente=0
valor_lineal=0
valor_ordenada=0
pendiente = ""
raiz = 0
delta=0
tipo_raiz=0
vertice_x=0
vertice_y=0
intervalo_crecimiento = ""
intervalo_decrecimiento = ""
b=0
raices = []
continuar = ""
valor_coheficiente_principal = 0
valor_ordenada_distinto = 0
valor_pendiente_perpendicular = 0
valores_independientes_distintos = []
comportamiento_recta=""
ecuacion = ""
con = 0
flag=0
op = ""
signo = ""

while(True):

    os.system("cls")

    if(flag==0):
        opcion = input("Bienvenidos al programa de operacion de ecuaciones matematicas! \n Elija la opcion que desee: \n 1) Rectas paralela y perpendicular a una dada. \n 2) Análisis de una función lineal.\n 3) Análisis de una función cuadrática. \n:")
    else:
        opcion = input("Ingrese una opcion valida \n 1) Rectas paralela y perpendicular a una dada. \n 2) Análisis de una función lineal.\n 3) Análisis de una función cuadrática. \n:")

    if(opcion.isnumeric()):
        opcion=int(opcion)
        if(opcion>3 or opcion<0):
            flag=1
    else:
        flag=1

    os.system("cls") 

    if opcion == 1 or opcion==2:

        flag = 0
        
        while(True):

            valor_pendiente= input("Ingrese el valor del coheficiente principal (siendo ax + b, ingrese el valor de a): ")

            if valor_pendiente == "0":
                print("Valor Invalido")
                continue
                
            try:
                valor_pendiente = Fraction(valor_pendiente)
                break                   
            except ValueError:
                print("Valor invalido")
                
        
        while(True):
    
            valor_ordenada= input("Ingrese el valor del termino independiente (siendo ax + b, ingrese el valor de b): ")    
            try:
                valor_ordenada = Fraction(valor_ordenada)
                break     
            except ValueError:
                print("Valor invalido")
        
        if(flag==0):

            if opcion==1:

                valores_independientes_distintos=[]
               
                while(con<3):

                    valor_ordenada_distinto = 0
                    valor_ordenada_distinto = random.randint(-20,20)

                    if(valor_ordenada_distinto!=valor_ordenada):
                        valores_independientes_distintos.append(valor_ordenada_distinto)
                        con+=1

                print("\nLa condicion de paralelismo es que el coheficiente principal se mantenga y el termino independiente sea el que cambie. \nEcuaciones con rectas paralelas a la dada:")
                con = 0
                
                while(con<3):
                    
                    if(valores_independientes_distintos[con]>0):
                        ecuacion = f"y = {Fraction(valor_pendiente)}x + {Fraction(valores_independientes_distintos[con])}"
                    else:
                        ecuacion = f"y = {Fraction(valor_pendiente)}x - {Fraction(valores_independientes_distintos[con])*(-1)} "
                    print(ecuacion)
                    con+=1

                print("\nLa condicion de perpendicularidad es que la pendiente debe ser inversa y opuesta, el termino independiente puede cambiar o no hacerlo. \nEcuaciones con rectas perpendiculares a la dada:")
                
                valor_pendiente_perpendicular = (1 / valor_pendiente) * (-1)
                
                con = 0
                if(valor_ordenada>=0):     
                    ecuacion = f"y = {Fraction(valor_pendiente_perpendicular)} x + {Fraction(valor_ordenada)}"
                else:
                    ecuacion = f"y = {Fraction(valor_pendiente_perpendicular)} x - {Fraction(valor_ordenada) * (-1)}"
                print (ecuacion)

                while(con<2):
                    if(valores_independientes_distintos[con]>=0):
                        ecuacion = f"y = {Fraction(valor_pendiente_perpendicular)} x + {Fraction(valores_independientes_distintos[con])}"
                    else:
                        ecuacion = f"y = {Fraction(valor_pendiente_perpendicular)} x - {Fraction(valores_independientes_distintos[con]) *(-1)}"
                    print(ecuacion)
                    con+=1
                    

                op=input("\n¿Desea seguir realizando operaciones con el programa? \nS/n \n:")
                if (op=="n" or op=="N"):
                    break
                

        
            if opcion==2:
                
                if(valor_pendiente>0):
                    pendiente = "Creciente"
                else:
                    pendiente = "Decreciente"

                if(valor_ordenada==0): 
                    raiz=0
                else:
                    # 0 = ax + b
                    # x = -b/a
                    raiz = (valor_ordenada * -1) / valor_pendiente
                    
                print("Corte en x = " + str(raiz))
                print("Corte en y = " + str(valor_ordenada))
                print("Pendiente = " + str(pendiente))

                op=input("\n¿Desea seguir realizando operaciones con el programa? \nS/n \n:")
                if (op=="n" or op=="N"):
                    break   
        
#Ejercicio 3

    if opcion==3:

        raices = []

        while(True):
 
            valor_pendiente = input("Ingrese el coheficiente principal. Siendo ax2 + bx + c ingrese el valor de a \n :")
            
            if valor_pendiente == "0":
                print("Valor Invalido")
                continue

            try:
                valor_pendiente = Fraction(valor_pendiente)
                break      
            except ValueError:
                print("Valor invalido")
            
        while(True):
            valor_lineal = input("Ingrese el termino lineal. Siendo ax2 + bx + c ingrese el valor de b \n :")

            try:
                valor_lineal = Fraction(valor_lineal)
                break      
            except ValueError:
                print("Valor invalido")
            
        while(True):

            valor_ordenada = input("Ingrese el termino independiente. Siendo ax2 + bx + c ingrese el valor de c \n :")
        
            try:
                valor_ordenada = Fraction(valor_ordenada)
                break      
            except ValueError:
                print("Valor invalido")
                                
        if(flag==0):

            if(valor_pendiente>0):
                pendiente = 1
            else:
                pendiente = -1

            delta = valor_lineal**2 - 4 * valor_pendiente * valor_ordenada
                

            if(delta>=0):

                raiz = ((valor_lineal * (-1)) + sqrt(delta)) / (2 * valor_pendiente)

                raices.append(raiz)

                raiz = ((valor_lineal * (-1)) - sqrt(delta)) / (2 * valor_pendiente)

                raices.append(raiz)


            vertice_x = (valor_lineal * -1) / (2 * valor_pendiente)

            vertice_y = valor_pendiente * vertice_x ** 2 + valor_lineal * vertice_x + valor_ordenada

            if(delta >= 0):

                print("Corte con el eje x: x1 = " + str(Fraction(raices[0])) + " x2 = " + str(Fraction(raices[1])))
                    
            print(f"Corte con el eje y: {valor_ordenada}")


            if(pendiente==1):
                
                intervalo_decrecimiento = "(-∞, " + str(vertice_x) + ")"  
                intervalo_crecimiento = "(" + str(vertice_x) + ", +∞)"
                
                print("El intervalo de decrecimiento es " + intervalo_decrecimiento)
                print("El intervalo de crecimiento es " + intervalo_crecimiento)
            
            elif(pendiente==-1):
                
                intervalo_crecimiento = "(-∞, " + str(vertice_x) + ")"  
                intervalo_decrecimiento = "(" + str(vertice_x) + ", +∞)"
                
                print("El intervalo de crecimiento es " + intervalo_crecimiento)
                print("El intervalo de decrecimiento es " + intervalo_decrecimiento)
            
    
            print("Los vertices son: Vx = " + str(vertice_x) + " Vy = " + str(vertice_y))

            print(f"La coordenada del vertice es ({vertice_x},{vertice_y})")

            if(valor_pendiente>0):
                print("La concavidad es hacia arriba ")

            elif(valor_pendiente<0):
                print("La concavidad es hacia abajo ")
        
            
            if(delta<0):
                print("Las raices son complejas ")

            elif(delta==0):
                print("Las raices son dobles ")

            elif(delta>0):
                print("Las raices son reales ")

            op=input("\n¿Desea seguir realizando operaciones con el programa? \nS/n \n:")

            if (op == "n" or op =="N"):
                break
        
        
        
        
        
    