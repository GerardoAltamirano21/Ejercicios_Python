def contar_vocales(frase):
	contador = 0
	for letra in frase:
		if letra.lower() in "aeiou":
			contador += 1
    
	return contador

frase = input("Ingrese una frase: ")
cantidad = contar_vocales(frase)
print(f"En la frase '{frase}' hay {cantidad} vocales")
