preguntas = [
    '¿Qué opina de Tangananica?',
    '¿Votaría por Mario para Core?, y para HardCore?',
    '¿Somos el curso favorito del profe?'
    
]
respuestas=[]
dicc_respuestas= {
    '1': 'Muy en desacuerdo',
    '2': 'En desacuerdo',
    '3': 'Ni de acuerdo ni en desacuerdo',
    '4': 'De acuerdo',
    '5': 'Muy deacuerdo'
}

def preguntar(pregunta):
    print('llegamos')
    print(pregunta)
    opciones='''
        Seleccione una de las siguientes
        1. Muy en desacuerdo
        2. En desacuerdo
        3. Ni de acuerdo ni en desacuerdo
        4. De acuerdo
        5. Muy deacuerdo
    '''
    
    
    eleccion = input(opciones)
    respuestas = dicc_respuestas[eleccion]
    respuestas.append({
        'pregunta': pregunta,
        'respuesta': eleccion
    })
    
    


def main():
    for pregunta in preguntas:
        preguntar(pregunta)

    print (respuestas)

main()