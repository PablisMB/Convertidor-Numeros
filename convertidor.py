# -*- coding: utf-8 -*-
# Versión: 1.0

import time
import webbrowser
import os, sys

print("Hecho por @PablisMB")

def main():
	print("Elige de que a que pasar el número")
	print("1. Decimal a binario")
	print("2. Binario a decimal")
	opcion = int(input("Elige una opción: "))
	
	def decimalABinario(numero_decimal):
		if(numero_decimal > 1):
			decimalABinario(numero_decimal//2)

		print(numero_decimal%2, end=' ')

	def binarioADecimal(numero_binario):
		numero_decimal = 0 

		for posicion, digito_string in enumerate(numero_binario[::-1]):
			numero_decimal += int(digito_string) * 2 ** posicion

		return numero_decimal

	if opcion == 1:
		numero_decimal = int(input("Introduce un número decimal: "))
		decimalABinario(numero_decimal)
		main()

	elif opcion == 2:
		numero_binario = input("Introduce un número binario: ")
		print(binarioADecimal(numero_binario))
		main()
	
	elif opcion == 69:
		print("Número gracioso")
		main()

	elif opcion == 727:
		print("Descubriste el easter egg XD CLV WYSI")
		time.sleep(1)
		webbrowser.open("https://www.youtube.com/watch?v=vatcanQQJvQ")
		main()

	else:
		print("Dije 1 o 2, pinche disléxico")
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