# Array 
# from array import *
import array as arr

# Creacion de un arreglo
# i: Entero con signo
# I: Entero sin signo
# f: Numero decimal
# d: Numero decimal doble
# u: Caracteres unicode
my_array = arr.array( 'i',[10,22,300])

#Interacion  automatica
for num in my_array:
    print (num)

# Acceso individual a los elementos
#print (my_array [0]) # Primer elemento
#print (my_array [1]) # Segundo elemento
# #print (my_array [1]) #  Tercer elemento

# tamaño  de un arreglo
# Lenght
#print( len (my_array))

# Iteracion por indices
for i in range (len(my_array)):
 if my_array [i]% 2 ==0:
    print(f" Elemento Num {i+1}: {my_array[i]} ")
