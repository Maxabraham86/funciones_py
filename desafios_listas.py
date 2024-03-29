import sys

def word_count():
    #1. obtenermos el nombre del archivo
    nombre_archivo = sys.argv[1]
    #2. leemos el contenido del archivo
    with open (nombre_archivo, 'r') as file:
        texto = file.read()
    #3. Contamos las letras y palabras
    texto_sin_espacio=[letra for letra in texto if letra!= ' ']
    print(f'En el archibo hay (sin contar espacios){len(texto_sin_espacio)}letras')
    #3.5 eliminamos duplicados
    #4. contamos las palabras
    lista_sin_duplicados= list(set(texto.split(' ')))
    num_palabras =len(lista_sin_duplicados)
    print(f'Hay {num_palabras} palabras.')
    #num_palabras = len(texto.split(' '))
    #print(f'Hay {num_palabras} palabras')
    #5. Contar caracteres
    caracteres= [letra for letra in texto]
    caracteres= set(caracteres)
    print(f'En el archivo hay {len(caracteres)} caracteres')
    
    
        
#word_count()





def conversiones():
    tasa_sol=float(sys.argv[1])
    tasa_ars=float(sys.argv[2])
    tasa_usd=float(sys.argv[3])
    peso_chileno= int(sys.argv[4])
    print(f'''
        los {peso_chileno} pesos equivalen a:
          {peso_chileno * tasa_sol} Soles
          {peso_chileno * tasa_ars} Pesos Agentinos
          {peso_chileno * tasa_usd} Dólares
        ''' )
    
conversiones()