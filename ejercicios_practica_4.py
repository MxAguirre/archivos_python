# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv

# Objetivo:
# Leer y trabajar con un archivo CSV complejo y el
# manejo de excepciones

def desafio(ambientes):
    
    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.
    
    # Según el valor ingresado en "ambientes" está función deberá
    # retornar (return):
    # 1) si ambientes == "2_ambientes"
    #  ---> retornar la cantidad encontrada de ddepartamentos de 2 ambientes
    # 2) si ambientes == "3_ambientes"
    #  ---> retornar la cantidad encontrada de ddepartamentos de 3 ambientes

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # Puede evitar que el programa explote utilizando "try except".

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    print('Ejercicios con archivos CSV complejos')
    
    archivo = open('propiedades.csv')
    data = list(csv.DictReader(archivo))
    archivo.close()
    cantidad_ambientes = ambientes[0]
    cantidad = 0

    for i in range(len(data)):
        depto = data[i]
        for k in depto.keys():
            if  k == 'ambientes':
                if cantidad_ambientes == data[i][k]:
                    cantidad += 1
    return cantidad

              
        
        

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print('Ingrese la cantidad de ambientes')
    ambientes = str(input('2 ambientes o 3 ambientes\n'))
    while ambientes != '2 ambientes' and ambientes != '3 ambientes':
        ambientes = str(input('Debe ingresar: 2 ambientes o 3 ambientes\n'))
    resultado = desafio(ambientes)
    print(f'La cantidad de deperatamentos de {ambientes} es {resultado}')
    