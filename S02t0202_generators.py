"" 
#Generators

#Los generadores son funciones que pueden 
#pausar su ejecucion

#Cuando se invoca una funcioon generadora
#devuelve un objeto   (aka Iterador)

#El codigo dentro de la funcion no sse ejecuta
#de inmediato , solo se compila

#La funcion se ejecuta unicamente cuando 
#iteras sobre el generador

" " " "

def my_generator ():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield 7
    yield 8
    yield 9
    yield 10
    yield 11
    yield 12
# Se invoca funcion generadora
my_iterator = my_generator()

# Se itera manualmente sobre el generador
#print(next(my_iterator)) # Imprime 1
#print(next(my_iterator)) # Imprime 2
#print(next(my_iterator)) # Imprime 3
#print(next(my_iterator)) # Imprime 4
#print(next(my_iterator)) # Imprime ?

# Los iteradores se pueden iterar con un for

for value in my_generator():
    print(value)




