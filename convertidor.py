# -*- coding: utf-8 -*-
# Versión: 1.1.1

import time
import webbrowser

print("Hecho por @PablisMB")
print("Versión 1.1.1")

print("")

def main():
	print("Elige de que a que pasar el número")
	print("1. Decimal a binario")
	print("2. Binario a decimal")
	print("3. Decimal a octal")
	print("4. Octal a decimal")
	print("5. Decimal a hexadecimal")
	print("6. Hexadecimal a decimal")
	print("7. Decimal a ASCII")
	print("8. ASCII a decimal")
	print("9. Texto a ASCII")
	print("10. Salir")
	print("")

	opcion = int(input("Elige una opción: "))
	
	def decimalABinario(numero_decimal):
		if numero_decimal <= 0:
			return "0"
		binario = ""
		while numero_decimal > 0:
			residuo = int(numero_decimal % 2)
			numero_decimal = int(numero_decimal / 2)
			binario = str(residuo) + binario
		print(binario)

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

	if opcion == 1:
		numero_decimal = int(input("Introduce un número decimal: "))
		decimalABinario(numero_decimal)
		main()

	elif opcion == 2:
		numero_binario = input("Introduce un número binario: ")
		print(binarioADecimal(numero_binario))
		main()
	
	elif opcion == 3:
		numero_decimal= int(input("Introduce un número decimal: "))
		print(decimalAOctal(numero_decimal))
		main()
	
	elif opcion == 4:
		numero_octal= input("Introduce un número octal: ")
		print(octalADecimal(numero_octal))
		main()

	elif opcion == 5:
		numero_decimal= int(input("Introduce un número decimal: "))
		print(decimalAHexadecimal(numero_decimal))
		main()

	elif opcion == 6:
		numero_hexadecimal= input("Introduce un número hexadecimal: ")
		print(hexadecimalADecimal(numero_hexadecimal))
		main()

	elif opcion == 7:
		numero_decimal= int(input("Introduce un número decimal: "))
		print(decimalAAscii(numero_decimal))
		main()

	elif opcion == 8:
		numero_ascii= input("Introduce un número ascii: ")
		print(asciiADecimal(numero_ascii))
		main()

	elif opcion == 9:
		string = input("Introduce un texto: ")
		print(stringAAscii(string))
		main()

	elif opcion == 10:
		print("*Inserta outro*")
		webbrowser.open("https://youtu.be/FX9eEhoRZhY?t=7")
		time.sleep(10)
		exit()

	elif opcion == 69:
		print("Número gracioso")
		main()

	elif opcion == 420:
		print("Número gracioso")
		main()

	elif opcion == 727:
		print("Descubriste el easter egg XD CLV WYSI")
		time.sleep(1)
		webbrowser.open("https://www.youtube.com/watch?v=vatcanQQJvQ")
		main()

	else:
		print("Pon una de las opciones pinche disléxico")
		print("Como pongas otra gilipollez te mato")
		opcion = (int(input("ELIGE EL PINCHE NÚMERO: ")))
		print("ERA BAIT XD")
		time.sleep(2)
		print("Valiste burguer")
		time.sleep(1)
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

main()