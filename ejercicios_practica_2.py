# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con diccionarios

import csv


def desafio():
    print('Ejercicio con diccionarios como base de datos')
    # Utilizaremos el diccionario como una base de datos. 
    # Comenzaremos con un diccionario de stock
    # de nuestros productos en cero:
    
    stock = {'tornillos': 0, 'tuercas': 0, 'arandelas': 0}

    # Paso 1:
    # Crear un bucle utilizando while que se ejecute de forma infinita
    # while True.....
    
    # Paso 2:
    # Dentro de ese bucle consultar al usuario por consola
    # que producto desea agregar al stock
    #   - Si el usuario ingresa "FIN" como producto se debe 
    #   finalizar el bucle
    #   - No debe agregar stock de productos que no estén
    #   definidos inicialmente en el diccionario stock.
    #   Para verificar si un producto existe dentro del
    #   diccionario stock utilice el operador "in" visto en clase

    # Paso 3:
    # Luego de haber ingresado el producto valido, se debe
    # ingresar por consola cuanto stock de ese producto se desea agregar.
    # Si teniamos 20 tornillos y el usuario desea agregar 10 tornillos más,
    # en nuestro diccionario deben quedar 30 tornillos (debe acumular)

    # Paso 4:
    # Cuando el usuario ingrese "FIN" y se termine el bucle, debe
    # imprimir en pantalla con print el diccionario con el stock final
    # Al final de esta función retornar (return) la variable stock

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    while True:
        agregar = str(input('¿Que desea agregar al stock? \n'))
        if agregar.lower() in stock:
            if agregar.lower() == 'tornillos':
                cantidad = input('Ingrese la cantidad\n')
                while cantidad.isdigit() == False:
                    print('Debe ingresar un valor numerico')
                    cantidad = input('Ingrese la cantidad\n')
                else:
                    total = stock['tornillos'] + int(cantidad)
                    stock['tornillos'] = total
                    continuar = str(input('Desea agregar algo mas?\n'))
                    while continuar != 'si' and continuar != 'fin':
                        continuar = str(input('Desea agregar algo mas?\n'))
                    if continuar == 'si':
                        pass
                    elif continuar == 'fin':
                        break            
            if agregar.lower() == 'tuercas':
                cantidad = input('Ingrese la cantidad\n')
                while cantidad.isdigit() == False:
                    print('Debe ingresar un valor numerico')
                    cantidad = input('Ingrese la cantidad\n')
                else:
                    total = stock['tuercas'] + int(cantidad)
                    stock['tuercas'] = total
                    continuar = str(input('Desea agregar algo mas?\n'))
                    while continuar != 'si' and continuar != 'fin':
                        continuar = str(input('Desea agregar algo mas?\n'))
                    if continuar == 'si':
                        pass
                    elif continuar == 'fin':
                        break
            if agregar.lower() == 'arandelas':
                cantidad = input('Ingrese la cantidad\n')
                while cantidad.isdigit() == False:
                    print('Debe ingresar un valor numerico')
                    cantidad = input('Ingrese la cantidad\n')
                else:
                    total = stock['arandelas'] + int(cantidad)
                    stock['arandelas'] = total
                    continuar = str(input('Desea agregar algo mas?\n'))
                    while continuar != 'si' and continuar != 'fin':
                        continuar = str(input('Desea agregar algo mas?\n'))
                    if continuar == 'si':
                        pass
                    elif continuar == 'fin':
                        break
        elif agregar == 'fin':
            print('No se agrego nada al stock')
            break
        else:
            print('Debe ingresar tornillos, tuercas o arandelas')
    print(stock)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    desafio()
