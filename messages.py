# This Python file uses the following encoding: utf-8
# Modulo para funcionabilidad de impresion de menus

# Importamos chalk para textos con colores (https://pypi.org/project/pychalk/)
# Importamos modulo os para limpiar la consola
import chalk
import os

# Limpia la pantalla
def clear():
  os.system('clear')

# Mensaje de inicio de saludo
def Wellcome ():
  clear()
  print(chalk.blue('\n████████████████████████████████████████████████████████████████████████████████ \n'))
  print(chalk.blue('                      ▀▄▒▄▀ ░░ ▒█▀▀█ ▒█▀▀█ ░█▀▀█ ▒█▀▀▀ ', bold=True ))
  print(chalk.blue('                      ░▒█░░ ▀▀ ▒█░▄▄ ▒█▄▄▀ ▒█▄▄█ ▒█▀▀▀ ', bold=True))
  print(chalk.blue('                      ▄▀▒▀▄ ░░ ▒█▄▄█ ▒█░▒█ ▒█░▒█ ▒█░░░ ', bold=True))
  print(chalk.blue('\n████████████████████████████████████████████████████████████████████████████████ \n'))



# Funcion para el menu principal envia al la variable op
def mainMenu ():
  print(chalk.blue('  typedata:   ', bold = True)+ 'Ingresar datos Manualmente')
  print(chalk.blue('  importdata: ', bold = True)+ 'Importar Datos de una direccion local ')
  print(chalk.blue('  editdata:   ', bold = True)+ 'Editar los datos ingresados / importados ')
  print(chalk.blue('  printdata:  ', bold = True)+ 'Imprimir tabla de datos ingresados')
  print(chalk.blue('  curve:      ', bold = True)+ 'Escojer un ajuste de curva para los datos ')
  print(chalk.blue('  exit:       ', bold = True)+ 'Salir...')
  return input('\n ► ')

# Funcion para el menu de curvas disponibles para la variable curve
def curvesMenu ():
  clear()
  Wellcome()
  print(chalk.blue('  1: ', bold = True)+ 'Regresion Polinomica grado N')
  print(chalk.blue('  2: ', bold = True)+ 'Regresion Logaritmica')
  print(chalk.blue('  3: ', bold = True)+ 'Regresion Exponencial')
  print(chalk.blue('  4: ', bold = True)+ 'Regresion Potencial')
  print(chalk.blue('  5: ', bold = True)+ 'Volver...')

  return input('\n ► ') 

