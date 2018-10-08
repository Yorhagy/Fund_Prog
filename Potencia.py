
def potencia (numeroEntero):
    k = 0
    resultado = numeroEntero
    parImpar = 0
    while (resultado !=1) and (parImpar == 0):
        resultado = resultado / 2
        parImpar = resultado % 2
        if resultado !=1 and parImpar !=0:
            return None
        k +=1
    return k  
#%%    
print (potencia(15))
print (potencia(4))
print (potencia(16))


    
