
def vocales (frase):
    contador = 0
    contadorc = 0
    for x in frase:
        if x in ('aeiouAEIOU'):
            contador +=1

        if x in ('bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'):
            contadorc +=1
    if contador > contadorc:
        print(f"las vocales {str(contador)} son mayores a las {str(contadorc)} consonantes")
    elif contador == contadorc :
        print(f"Las {str(contador)} vocales son de igual cantidad que las {str(contadorc)} consonantes")
    else:
        print(f"las {str(contadorc)} consonates son mayores a las {str(contador)} vocales \n")
    s = (str(contador) + " vocales y " + str(contadorc) + " consonantes encontradas en toda la frase")
    return s
a = input("Ingresar una frase : ")
print(vocales(a))
