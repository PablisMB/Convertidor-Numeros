# -*- coding: utf-8 -*-
# Versión: 1.3

from colorama import init
import logging
import os
import time
import webbrowser

logging.error("Error inesperado", exc_info=True)

init()
init(autoreset=True)

class style():
	NEGRO = '\033[90m'
	ROJO = '\033[91m'
	ROJO_SANGRE = '\033[31m'
	VERDE = '\033[92m'
	AMARILLO = '\033[93m'
	AZUL = '\033[94m'
	MAGENTA = '\033[95m'
	CYAN = '\033[96m'
	BLANCO = '\033[97m'
	SUBRAYADO = '\033[4m'
	BOLD = '\033[1m'
	RESET = '\033[0m'

def logo():
	os.system("cls")
	print(style.CYAN + '''                      .o8       oooo   o8o                              .o8       
                     "888       `888   `"'                             "888       
oo.ooooo.   .oooo.    888oooo.   888  oooo   .oooo.o ooo. .oo.  .oo.    888oooo.  
 888' `88b `P  )88b   d88' `88b  888  `888  d88(  "8 `888P"Y88bP"Y88b   d88' `88b 
 888   888  .oP"888   888   888  888   888  `"Y88b.   888   888   888   888   888 
 888   888 d8(  888   888   888  888   888  o.  )88b  888   888   888   888   888 
 888bod8P' `Y888""8o  `Y8bod8P' o888o o888o 8""888P' o888o o888o o888o  `Y8bod8P' 
 888                                                                              
o888o                                                                             
                                                                                  ''')
	print("")

	print(style.VERDE + "Versión 1.3")
	print("")

def main():
	print(style.AZUL + "Elige de que a que pasar el número")
	print("")
	print(style.BOLD + "1. Decimal a binario")
	print(style.BOLD + "2. Decimal a octal")
	print(style.BOLD + "3. Decimal a hexadecimal")
	print(style.BOLD + "4. Decimal a ASCII")
	print(style.BOLD + "5. Binario a decimal")
	print(style.BOLD + "6. Octal a decimal")
	print(style.BOLD + "7. Hexadecimal a decimal")
	print(style.BOLD + "8. ASCII a decimal")
	print(style.BOLD + "9. Texto a ASCII")
	print(style.BOLD + "10. ASCII a texto")
	print(style.BOLD + "11. Todo en uno")
	print("")
	print(style.AMARILLO + "12. Opciones")
	print("")
	print(style.ROJO + "0. Salir")
	print("")

	opcion = int(input(style.VERDE + "Elige una opción: "))
	print("")
	
	os.system("")

	style()

	def decimalABinario(numero_decimal):
		if numero_decimal < 0:
			return '-' + decimalABinario(abs(numero_decimal))
		elif numero_decimal == 0:
			return '0'
		else:
			return decimalABinario(numero_decimal // 2) + str(numero_decimal % 2)

	def binarioADecimal(numero_binario):
		numero_decimal = 0 

		for posicion, digito_string in enumerate(numero_binario[::-1]):
			numero_decimal += int(digito_string) * 2 ** posicion

		return numero_decimal

	def decimalAOctal(numero_decimal):
		octal = ""
		while numero_decimal > 0:
			residuo = numero_decimal % 8
			octal = str(residuo) + octal
			numero_decimal = int(numero_decimal / 8)
		return octal

	def octalADecimal(numero_octal):
		decimal = 0
		posicion = 0
		numero_octal = numero_octal[::-1]
		for digito in numero_octal:
			valor_entero = int(digito)
			numero_elevado = int(8 ** posicion)
			equivalencia = int(numero_elevado * valor_entero)
			decimal += equivalencia
			posicion += 1

		return decimal

	def decimalAHexadecimal(numero_decimal):
		hexadecimal = ""
		while numero_decimal > 0:
			residuo = numero_decimal % 16
			if residuo == 10:
				residuo = "A"
			elif residuo == 11:
				residuo = "B"
			elif residuo == 12:
				residuo = "C"
			elif residuo == 13:
				residuo = "D"
			elif residuo == 14:
				residuo = "E"
			elif residuo == 15:
				residuo = "F"
			hexadecimal = str(residuo) + hexadecimal
			numero_decimal = int(numero_decimal / 16)
		return hexadecimal

	def hexadecimalADecimal(numero_hexadecimal):
		decimal = 0
		posicion = 0
		numero_hexadecimal = numero_hexadecimal[::-1]
		for digito in numero_hexadecimal:
			if digito == "A":
				digito = 10
			elif digito == "B":
				digito = 11
			elif digito == "C":
				digito = 12
			elif digito == "D":
				digito = 13
			elif digito == "E":
				digito = 14
			elif digito == "F":
				digito = 15
			valor_entero = int(digito)
			numero_elevado = int(16 ** posicion)
			equivalencia = int(numero_elevado * valor_entero)
			decimal += equivalencia
			posicion += 1

		return decimal

	def decimalAAscii(numero_decimal):
		ascii = chr(numero_decimal)
		return ascii

	def asciiADecimal(numero_ascii):
		decimal = ord(numero_ascii)
		return decimal
	
	def stringAAscii(string):
		ascii = ""
		for i in string:
			ascii = ascii + str(ord(i)) + " "
		return ascii

	def asciiAString(ascii):
		string = ""
		for i in ascii.split():
			string = string + chr(int(i))
		return string

	def todoEnUno():
		numero = int(input("Introduce el número: "))
		print("")
		print("El número en binario es: " + style.BOLD + str(decimalABinario(numero)))
		print("")
		print("El número en octal es: " + style.BOLD + str(decimalAOctal(numero)))
		print("")
		print("El número en hexadecimal es: " + style.BOLD + str(decimalAHexadecimal(numero)))
		print("")
		print("El número en ASCII es: " + style.BOLD + str(decimalAAscii(numero)))
		print("")

	if opcion == 1:
		numero_decimal = int(input("Introduce un número decimal: "))
		print(decimalABinario(numero_decimal))
		print("")
		main()

	elif opcion == 2:
		numero_decimal = int(input("Introduce un número decimal: "))
		print(decimalAOctal(numero_decimal))
		print("")
		main()

	elif opcion == 3:
		numero_decimal = int(input("Introduce un número decimal: "))
		print(decimalAHexadecimal(numero_decimal))
		print("")
		main()		

	elif opcion == 4:
		numero_decimal = int(input("Introduce un número decimal: "))
		print(decimalAAscii(numero_decimal))
		print("")
		main()

	elif opcion == 5:
		numero_binario = (input("Introduce un número binario: "))
		print(binarioADecimal(numero_binario))
		print("")
		main()
	
	elif opcion == 6:
		numero_octal = (input("Introduce un número octal: "))
		print(octalADecimal(numero_octal))
		print("")
		main()

	elif opcion == 7:
		numero_hexadecimal = (input("Introduce un número hexadecimal: "))
		print(hexadecimalADecimal(numero_hexadecimal))
		print("")
		main()

	elif opcion == 8:
		numero_ascii = input("Introduce un texto en ASCII: ")
		print(asciiADecimal(numero_ascii))
		print("")
		main()

	elif opcion == 9:
		string = input("Introduce un texto: ")
		print(stringAAscii(string))
		print("")
		main()

	elif opcion == 10:
		ascii = input("Introduce un texto en ASCII: ")
		print(asciiAString(ascii))
		print("")
		main()

	elif opcion == 11:
		todoEnUno()
		main()

	elif opcion == 12:
		print(style.BOLD + "1. Limpiar consola")
		print(style.BOLD + "2. Cambiar color de la consola")
		print(style.BOLD + "3. Mostrar página de GitHub")
		print(style.BOLD + "4. Volver al menú principal")
		print("")

		opcion_o = int(input(style.VERDE + "Elige una opción: "))

		if opcion_o == 1:
			os.system("cls")
			logo()
			main()

		elif opcion_o == 2:
			print(style.VERDE + "No te creas hacker :v")
			time.sleep(2)
			print("")
			main()

		elif opcion_o == 3:
			webbrowser.open("https://github.com/PablisMB/Convertidor-Numeros")
			print("")
			main()
		
		elif opcion_o == 4:
			print("")
			main()

	elif opcion == 0:
		print(style.VERDE + "*Inserta outro*")
		webbrowser.open("https://youtu.be/FX9eEhoRZhY?t=7")
		time.sleep(10)
		exit()

	elif opcion == 69:
		print(style.VERDE + "Número gracioso")
		print("")
		main()

	elif opcion == 420:
		print(style.VERDE + "Número gracioso")
		print("")
		main()

	elif opcion == 666:
		print(style.ROJO_SANGRE + "Tai, Tai estás ahí?")
		print("")
		time.sleep(3)
		print(style.ROJO_SANGRE + "Tai, Tai estás ahí?")
		print("")
		time.sleep(3)
		main()

	elif opcion == 727:
		print(style.AZUL + "Descubriste el easter egg XD CLV WYSI")
		time.sleep(1)
		webbrowser.open("https://www.youtube.com/watch?v=vatcanQQJvQ")
		print("")
		main()

	elif opcion == 911:
		print(style.ROJO_SANGRE + "TOTALMENTE NO ES UNA REFERENCIA A UN DIA EN CONCRETO")
		time.sleep(5)
		print("")
		print(style.BOLD + "No towers? No WTC? 9/11? Football > Soccer")
		time.sleep(0.3)
		os.system("cls")
		logo()
		main()

	elif opcion == 42069:
		print(style.AMARILLO + "Número muy gracioso")
		print("")
		main()

	elif opcion == 69420:
		print(style.AMARILLO + "Número muy gracioso")
		print("")
		main()

	elif opcion == 72769420:
		print(style.AMARILLO + "Bienvenido a TaiBombs")
		time.sleep(1)
		webbrowser.open("https://taibombs.webnode.es")
		print("")
		main()

	else:
		print(style.ROJO_SANGRE + "Pon una de las opciones pinche disléxico")
		print(style.ROJO_SANGRE + "Como pongas otra gilipollez te mato")
		opcion = input(style.ROJO_SANGRE + "ELIGE EL PINCHE NÚMERO: ")
		print(style.MAGENTA + "ERA BAIT XD")
		time.sleep(2)
		print(style.ROJO + "Chau PC en 5")
		time.sleep(1)
		print(style.ROJO + "4")
		time.sleep(1)
		print(style.ROJO + "3")
		time.sleep(1)
		print(style.ROJO + "2")
		time.sleep(1)
		print(style.ROJO + "1")
		time.sleep(1)
		print(style.ROJO_SANGRE + "Valiste burguer")
		time.sleep(1)
		print(style.CYAN + "WAZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
		time.sleep(0.5)
		webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=1, autoraise=True)
		webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=1, autoraise=True)
		webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=1, autoraise=True)
		webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=1, autoraise=True)
		webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=1, autoraise=True)
		webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=1, autoraise=True)
		webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=1, autoraise=True)
		webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=1, autoraise=True)
		webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=1, autoraise=True)
		webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=1, autoraise=True)
		exit()
		
logo()
main()