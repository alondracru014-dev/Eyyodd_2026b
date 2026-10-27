from array import array as arr

# Paramentros de mi cuadricula 
rows = 3
columns = 2 * rows - 1

#Funcion para imprimir matrix
def print_matrix(input_matrix):
  for row in matrix:
   print(list(row))   
#Creando la reticula(grid) 2D Bidimensional 
matrix = []
#Construyendo la rejilla(grid)
for _ in range(rows):
    new_row = arr('i', [0]* columns)
    matrix.append(new_row)  

#Validando la construccionn del grid
print(f"Cantidad de filas: {len(matrix)}")
print(f"Cantidad de columnas: {len(matrix[0])}")

#Calculando el centro de la primera fila
center = columns // 2 # cuando ponemos doble // es para que sea  divicion entera 

#Estableciendo el centro en 1
matrix[0][center] = 1 #fila es la primera y la columna es la que da pie 

print_matrix(matrix)

# Se calcula el resto de la matrix
# Siguiendo la logica del siperpinsky Gasket
for row in range (1,rows):
    for column in range (0,columns):
         left_upper_cell=0
         right_upper_cell=0


# Si la columna  donde estamos
# Es mayor a cero es decir esta un elemento
# Despues del borde izquierdo
if column > 0:
 left_upper_cell = matrix [row-1][column-1]

 # Si la columna esta un elemento antes
 # Del borde derecho
 if column < columns -1:
    right_upper_cell = matrix [row-1][column+1]

    # Guardo el arreglo
    if left_upper_cell  != right_upper_cell
     matrix[row][column] = 1
    else:
       matrix [row][column]=0

print()
print_matrix(matrix)
