
def cadena(caracteres):
    largo = len(caracteres)
    k = 1
    copia = caracteres
    copia = list(copia)
    for letra in caracteres:
        if letra.isalpha():
            copia[largo-k] = caracteres[k-1]
        else:
            copia[k-1] = letra
        k +=1
    return print (str(copia))

cadena("13xz&ih87jkg=$qa1")



