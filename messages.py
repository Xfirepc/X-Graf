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
  print(chalk.blue('     ooooo  oooo             ooooooo8  oooooooooo       o      ooooooooooo ', bold=True ))
  print(chalk.blue('       888  88             o888    88   888    888     888      888    88 ', bold=True))
  print(chalk.blue('         888     ooooooooo 888    oooo  888oooo88     8  88     888ooo8    ', bold=True))
  print(chalk.blue('        88 888             888o    88   888  88o     8oooo88    888        ', bold=True))
  print(chalk.blue('     o88o  o888o            888ooo888  o888o  88o8 o88o  o888o o888o   ', bold=True))
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

