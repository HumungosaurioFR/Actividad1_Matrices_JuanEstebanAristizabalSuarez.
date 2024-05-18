import os

matriz1 = [['◉','◉','◉','◉','◉'],
           ['◉','◉','◉','◉','◉'],
           ['◉','◉','◉','◉','◉'],
           ['◉','◉','◉','◉','◉'],
           ['◉','◉','◉','◉','◉']]
correcto = '😁'
incorrecto = '💀'
ls_pregunta = ['¿Qué es python?\n\n1. Juego\n2. Lenguaje de Programación\n3. Maraca de Autos\n4. Ninguna de las Anteriores','¿Qué es HTML?\n\n1. Lenguaje de Etiquetas\n2. Marca de Gaseosas\n3. Un Navegado\n4. Una que Suda']
ls_respuestas = ['2','1']


def fnt_limpiar():
    os.system('cls')
    print('Autor: Juan Aristizábal\nFecha: 9 de abril del 2024\n')

def fnt_impresion_matriz():
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            print(matriz1[i][j], end='      ')
        print('\n\n')
    
contador = 0
    
for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            fnt_limpiar()
            fnt_impresion_matriz()
            print()
            print(ls_pregunta[contador])
            print()
            r = input('->')
            if r == ls_respuestas[contador]:
                matriz1[i][j] = correcto
                contador += 1
            else:
                matriz1[i][j] = incorrecto

                contador += 1