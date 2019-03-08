# This Python file uses the following encoding: utf-8
# Importamos funciones a utilizar del modulo2
# Importamos funciones del modulo 1
from functionsMat import table, dataX, dataY, validateData, editMatrix, fillMatrixData
from messages import clear, Wellcome, mainMenu, curvesMenu

# Importamos numpy, matplotlib, scipy y math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math

# Operador del menu principal
op = ''

def grafPolinomy( matrix, grade):
  X = []
  Y = matrix['y']
  puntosX = matrix['x']

  for data in range(int(matrix['data'])):
    X.append([])
    for val in range(grade):
      X[data].append((puntosX[data] ** val))
      
  return {'vecy': np.matrix(Y), 'coefx': np.matrix(X)}
      


# Calcula de forma matricial los coeficientes de vectores de puntos X y Y
def calcMatrix(vecx, vecy):
  
  print("\n ✘✘ Matriz de ajuste de polinomio: \n")
  print(vecx)
  print("\n ✘✘ Matriz de datos en Y: \n")
  print(vecy)

  X = np.array(vecx)
  Y = np.array(vecy)
  K = np.dot(np.transpose(X), X)
  V = np.dot(Y,X)
  return np.dot(np.linalg.inv(K), np.transpose(V))

def rd(num):
  return round(num,5)

# -------------------------------------------------------------------------------
# Inicio del programa para el menu principal.
# -------------------------------------------------------------------------------

#Vatiable para saber si se ingreso datos..
fillTable = False

while True: 

  Wellcome()      #Lanzamos el saludo
  op = mainMenu() #Recibimos opcion del menu 1 

  # Opcion 1 TypeData
  # Ingrasara datos por teclado 
  if op == 'typedata':
    print('\n ✘✘ Ingrese los valores de X & Y para los datos x para salir:  \n')
    recivedData = fillMatrixData(False)
    fillTable = True

  # Opcion 2 Importdata
  # Ingrasara datos mediante un path del archivo y el delimitador
  if op == 'importdata':
    path = input(' ✘✘ Ingrese la direccion del archivo ►  ')
    delimit = input(' ✘✘ Ingrese el delimitador de datos ►  ')
    data = np.loadtxt(path, delimiter = delimit)

    print('\n ✘✘ Los datos importados son: \n')
    recivedData = fillMatrixData(data.tolist())
    print(table(recivedData['x'], recivedData['y']))
    fillTable = True


  # Opcion 3 Editdata
  # Editara la matriz con el algoritmo editMatrix()
  if (fillTable and op == 'editdata'):
    recivedData['matriz'] = editMatrix(recivedData['matriz'])
    recivedData = fillMatrixData(recivedData['matriz'])


  # Opcion 4 Printdata
  # Imprimira los datos con la funcion table del modulo 1
  if (fillTable and op == 'printdata'):
    print('\n Los datos ingesados son: \n')
    print(table(recivedData['x'], recivedData['y']))



  # Opcion 5 Cruve
  # Lanzara el otro menu del modulo 1 curvesMenu()
  # Se divide en partes para cada ajuste de curva
  if (fillTable and op == 'curve'):

    # Inicializo los puntos y matriz para comenzar a trabajar
    # Variables importantes  x, y, xp
    Wellcome()
    curve = int(curvesMenu())

    recivedData = fillMatrixData(recivedData['matriz'])
    x = np.array(recivedData['x'])
    y = np.array(recivedData['y'])
    xp = np.linspace(0.1, max(x), 100)

    # Ajuste polinomico..
    if(curve == 1):
      clear()
      Wellcome()
      grado = int(input('\n Grado del polinomoio: ► '))

      #Calculamos los datos de coeficientes mediante operacion matricial calMatrix()
      mat  = grafPolinomy(recivedData, grado + 1 )
      S = calcMatrix(mat['coefx'], mat['vecy'])

      print("\n ✘✘ Matriz de coeficientes de grado [", grado ,"] \n")
      print(S)

      z = np.polyfit(x, y, grado)
      p = np.poly1d(z)

      #Preparamos el plot para comenzar a graficar
      print('\n Ecuacion: Y = ', p)
      plt.title("REGRESIÓN POLINÓMICA")
      plt.plot(xp, p(xp), label = p)
      plt.legend(loc="upper left")

      slope, intercept, r_value, p_value, std_err = stats.linregress(y, x)
      print('\n R_cuadrado: ',r_value**2)


    # Ajuste Logaritmico
    if(curve == 2):
      clear()
      Wellcome()

      z = np.polyfit(np.log(x), y, 1)
      ec = "Y =" + str(rd(z[0])) + "ln(x) + " + str(rd(z[1]))
      print('\n Ecuacion: ', ec)

      def flog(x):
        return z[0]*np.log(x) + z[0]
      
      plt.title("REGRESIÓN LOGARITMICA")
      plt.plot(xp, [flog(i) for i in xp], label = ec)
      plt.legend(loc="upper left")

      nx = []
      for i in range(0,len(x)):
	      nx.append(math.log(x[i]))
      slope, intercept, r_value, p_value, std_err = stats.linregress(y, nx)
      print('\n R_cuadrado: ',r_value**2)

    # Ajuste Exponencial
    if(curve == 3):
      clear()
      Wellcome()

      z = np.polyfit(x, np.log(y), 1, w = np.sqrt(y))

      a = round(z[0],4)
      b = round( np.exp(z[1]),4)
      ec = 'Y = ' + str(rd(b)) + 'e^(' + str(rd(a)) + 'x)'
      print('\n Ecuacion:  Y=',b,'e','^','(',a,')','x')

      def fexp(x):
        return b*(2.718281**(a*x))

      plt.title("REGRESIÓN EXPONENCIAL")
      plt.plot(xp, [fexp(i) for i in xp], label = ec)
      plt.legend(loc="upper left")

      nx = []
      for i in range(0,len(x)):
	      nx.append(np.exp(x[i]))
      slope, intercept, r_value, p_value, std_err = stats.linregress(y, nx)
      print('\n R_cuadrado: ',r_value**2)


    if(curve == 4):
      clear()
      Wellcome()

      x = x.tolist()
      y = y.tolist()
      
      sumlogy = sum(math.log10(y[i]) for i in range(len(x))) 
      sumlogx = sum(math.log10(x[i]) for i in range(len(x))) 
      sumxy = sum(math.log10(x[i])*(math.log10(y[i])) for i in range(len(x))) 
      sumlogx2 = sum(math.log10(x[i])**2 for i in range(len(x))) 
      incognitas = np.array([[len(x),sumlogx],[sumlogx, sumlogx2]])
      valores = np.array([sumlogy, sumxy])

      res = np.linalg.solve(incognitas, valores)

      a = np.power(10, res[0])
      b = res[1]
      ec = 'Y = ' + str(rd(a)) + 'X^' + str(rd(b)) 
      print('Ecuacion: Y = ',a,'X^',b)

      def fpow(x):
        return a*x**b

      plt.title("REGRESIÓN POTENCIAL")
      plt.plot(xp, [fpow(i) for i in xp], label = ec)
      plt.legend(loc="upper left")

      nx = []
      for i in range(0,len(x)):
	      nx.append(np.exp(x[i]))  
      slope, intercept, r_value, p_value, std_err = stats.linregress(y, nx)
      print('\n R_cuadrado: ',r_value**2)

  
    # Preparacion e impresion del plot con los datos
    plt.ylabel("Datos en Y") 
    plt.xlabel("Datos en X") 
    plt.plot(x, y, 'p')
    plt.show()

    if(curve == 5):
      break

  input('\n ✘✘ Presione Enter...')
  if op == 'exit':
    break
  else: 
    print('\n ✘✘ Opcion incorrecta o aun no has ingresado datos.. ✘✘')

