#1. .item()
import sys
'''
umbral= sys.argv[1]
mayor_menor= ''
if len(sys.argv)>2:
    if sys.argv[2] == "menor":
        mayor_menor="menor"
    else:
        print('Lo sentimos, no es una operación valida')
        sys.exit()
else:
    mayor_menor= "mayor"
    
    
def filtroc(umbral, mayor_menor = "mayor"):
    precios = {
        'Notebook': 700000,
        'Teclado': 25000,
        'Mouse': 12000,
        'Monitor': 250000,
        'Escritorio': 135000,
        'Tarjeta de Video': 1500000
    }
    
    productos_filtrados=[]
    
    if mayor_menor =="mayor":
        for producto, precio in precios.items():   
            if precio > int(umbral):
                productos_filtrados.append(producto)
        impresion_productos = ','.join(productos_filtrados)
        print(f'los productos mayor al umbral son: {impresion_productos}')    
    else:
        for producto, precio in precios.items():   
            if precio < int(umbral):
                productos_filtrados.append(producto)
        impresion_productos = ','.join(productos_filtrados)
        print(f'los productos mayor al umbral son: {impresion_productos}')
        

filtroc(umbral,mayor_menor)
#2. enumetare()


velocidades = [
    25, 12, 19, 16, 11, 11, 24, 1,
    14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
    14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
    14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
    10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
    11, 10, 18, 10, 14, 5, 23, 20, 23, 21]
    

promedio = 0
for velocidad in velocidades:
        promedio += velocidad
promedio = promedio/len(velocidades)

posiciones = []

for index, item in enumerate(velocidades):
    if item >= promedio:
        posiciones.append(index)
print(posiciones)
        

'''

def factorial_iterativo(n):
    resultado=1
    for i in range(1,n+1):
        resultado*= i
    return resultado
numero=int(input('Introduce un número entero para calcular su factorial: '))
resultado = factorial_iterativo(numero)
print('El factorial de', numero, 'es', resultado)




def productoria(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado


numeros = [4,6,7,4,3]
resultado = productoria(numeros)
print ('La productoria de los numeros', numeros,'es', resultado)


def calcular(fact_1, prod_1, fact_2):
    resltf1 = factorial_iterativo(fact_1)
    restp = productoria(prod_1)
    restf2 = factorial_iterativo(fact_2)
    print(f'el valor del factorial 5 es:{resltf1}, de la productoria{restp} y el factorial de 6 es {restf2}')

calcular(fact_1 = 5, prod_1=[4,6,7,4,3], fact_2 = 6)
'''
def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

def productoria(lista_valores):
    producto = 1
    for i in lista_valores:
        producto *= i
    return producto

def calcular(fact_1, prod_1, fact_2):
    resultado_factorial1 = factorial(fact_1)
    resultado_productoria = productoria(prod_1)
    resultado_factorial2 = factorial(fact_2)
    print(f'El factorial de {fact_1} es {resultado_factorial1}')
    print(f'La productoria de {prod_1} es {resultado_productoria}')
    print(f'El factorial de {fact_2} es {resultado_factorial2}')

calcular(fact_1 = 5, prod_1 = [4,6,7,4,3], fact_2 = 6)




def factorial_iterativo(n):
    resultado=1
    for i in range(1,n+1):
        resultado*= i
    return resultado
numero=int(input('Introduce eun número entero para calcular su factorial: '))
resultado = factorial_iterativo(numero)
print('El factorial de', numero, 'es', resultado)
'''