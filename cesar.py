texto_original = input("Texto original: ")
texto_codificadocodificado = ""

for letra in texto_original:
	texto_codificado += texto_codificado + chr(ord(letra) + 6)
    
print("Texto codificado: ",texto_codificado)
