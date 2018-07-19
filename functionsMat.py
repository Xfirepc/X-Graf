
# Importamos modulo tabulate (https://pypi.org/project/tabulate/)
# Importamos el modulo messages ques creamos antes..
from tabulate import tabulate
from messages import clear

# Usando el modulo tabulate realizo una tabla con puntos x & y que son listas
def table(puntosX, puntosY):
  return tabulate({'Fila': range(1, len(puntosX) + 1), 'Datos X': puntosX, 
                    'Datos Y': puntosY}, headers = "keys", tablefmt="fancy_grid")

# Defino 2 funciones para romper una matriz de X y Y que retorna los valores en una lista
def dataX(matrix):
  x = []
  for i in range(len(matrix)):
    x.append(matrix[i][0])
  return x

def dataY(matrix):
  y = []
  for i in range(len(matrix)):
    y.append(matrix[i][1])
  return y

# Funcion para validad entrada de datos numericos
# Si se ingresa x termina el bucle...
def validateData ( num ):
  while True:
    if num.isdigit(): break
    elif num == 'x': return -1
    else: num = input('Valor?: ')

  return float( num )

# Funcion para editar datos de una matriz
# Pide al usuario la posicion de la fila en la matriz y cambia los valores
# Retorna otra matriz editada..
def editMatrix( matrix ):

  print("\n ✘✘ Ingrese la posicion que desea editar: \n")
  x = dataX(matrix)
  y = dataY(matrix)
  print(table(x, y))

  row = int(validateData(input(' Fila:  ')))
  print(' ', matrix[row -1], '\n')

  for i in range (2):
    matrix[row - 1][i] = validateData(input(' Col[{}]:  '.format(i)))

  return matrix


# Funcion mas importante...
# Rellena una matriz validando datos 
# Rellena una matriz validando datos 
# Retorna un diccionario con:
# Puntos en X & Y
# Matriz de los puntos y numero de datos 
def fillMatrixData ( imported ):
  matrix, puntosX, puntosY = [], [], []
  go = True
  data = 0
  # En caso de recibir datos por importacion de numpy le preguntamos es reutilizable
  if imported:
    data = len(imported)
    matrix = imported
    puntosX = dataX(matrix)
    puntosY = dataY(matrix)

  else:
    # Agrega datos a una lista hasta presionar letra x
    while(go):
        matrix.append([])
        for j in range( 2 ):
          if (j == 0):
            matrix[ data ].append(validateData(input(' [ X ]: ')))
          else:
            matrix[ data ].append(validateData(input(' [ Y ]: ')))
          if(matrix[ data ][j] == -1):
            go = False
            break
        data += 1

    data = data - 1

    # Eliminar los ultimos elementos de la matriz y vectores para salir del blucle
    matrix.pop()
   
    while True: 
      puntosX = dataX(matrix)
      puntosY = dataY(matrix)

      clear()
      print("\n ✘✘ La Tabla de datos ingresada es: \n")
      print( table(puntosX, puntosY) )
      
      # Edita la matriz despues de ingresarse
      editar = input('\n Desea editar un dato? (y/n): ► ')

      if editar == 'y':
        matrix = editMatrix(matrix)
      if editar =='n':
          break
      else:
        print('\n ✘✘ Ingresa (y o n) para si o no.. ✘✘')

    puntosX = dataX(matrix)
    puntosY = dataY(matrix)
  #Retorna los puntos x & y la matriz completa y el numero de datos..
  return { 'x': puntosX, 'y': puntosY, 'matriz': matrix, 'data': data }