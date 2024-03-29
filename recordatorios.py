'''

recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"]]


# Output
recordatorios.insert(1,["2021-02-02. '06:00', 'Empezar el año'"])

recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])
indice_julio_15 = recordatorios.index(['2021-07-15', '13:00', 'No hacer nada es feriado'])
recordatorios[indice_julio_15][0] = '2021-07-16'
#recordatorios.insert(2,['2021-07-16', '13:00', 'No hacer nada es feriado'])
#recordatorios.remove(['2021-07-15', "13:00", "No hacer nada es feriado"])
recordatorios.insert(5,['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.remove(['2021-05-01', "15:00", "No trabajar"])


#otra  alternativa vista en clases

eventonuevo=["2021-02-02. '06:00', 'Empezar el año'"]

recordatiorios = [recordatorios[0], eventonuevo] + recordatorios[1:]

#print(recordatorios)


eventos [
    ['2022-09-18', '20:00', 'Bailar cueca'],
    ['2022-01-03', '21:00', 'Se te aparecio marzo'],
    ['2022-01-01', '07:00', 'Salir a correr']
]

eventos.sort(CRITERIO)

esta funcion no retorna
sólo imprime

def promedio(num1, num2, num3):
    prom= (num1+num2+num3)/3
    print (prom)
    

esta funcion si retorna 
    
    def promedio(num1, num2, num3):
    prom= (num1+num2+num3)/3
    return prom
    
    print('El promedio de 5,6,7 es ' str(promedio(5,6,7)))
    
    
def suma (a,b):
    return a+b
def porDos(x):
    return 2*x
def divCinco(x):    
    return x/5
    
    #las funciones que retornan algo que puede ser usado en otras lineas
    
    suma(porDos(divCinco)10)),10)
    
    def validarNombre(nombre):
        if len(nombre)<2:
            return False
        elif len(nombre) > 20:
            return False
        elif isMayuscula(nombre[0])
            return False
        return True
            

'''

    
#en este caso "Anonimo" es el parametro por defecto
def buenos_modales(nombre = "Anonimo"):
    hola = "Buenos dias "+ nombre
    chao = "nos vemos " + nombre    
    return hola, chao
#El retorno múltiple es una tupla con str
#desempaquetar la tupla
saludo, adios = buenos_modales()
'''
palabras = buenos_modales('Matias')
saludo= palabras[0]
adios = palabra[1]
'''

print(saludo)
print(adios)

