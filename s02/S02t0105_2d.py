from array import array as arr


#impresion de de una tabla
def print_table(table):
    #imprimiendo cada elemento
    for row in table:
        for column in row:
            print(column, end=",")
        print("\b" )

table = [
    arr('i', [1,2,3]),
    arr('i', [4,5,6]),
    arr('i', [7,8,9]),
]
print_table(table)
#insercion
row = 1
column = 2
value = 99

#insertar en la fila 1 columna 2 el valor 99
table[row].insert(column, value)

#imprimiendo mensaje
print(f"---Despues de la insercion ---")
print_table(table)#DRY

# Imprimiendo una fila completa
new_row = arr('i',[100,200,300])
pos=1
table.insert (pos,new_row)

#Imprimiendo mensaje
print (f"--- Despues de la insercion de una fila completa---")
print_table(table)#DRY


# Eliminacion de elementos
del table[2]

#Imprimiendo mensaje
print(f"---Despues de la eliminados de la fila 2---")
print_table(table)#DRY





