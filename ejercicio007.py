# Al enumerar los primeros seis números primos: 2, 3, 5, 7, 11 y 13, podemos ver que el sexto primo es 13.
# ¿Cuál es el número primo 10 001?
#----------------------------------------------
def primo(nro):
    nro=nro
    for i in range(2,nro):
        if nro%i==0:
            return False
    return True
#-------------------
# primo(10)
#-------------------
def arrayPrimo(nro):
    primos =[]
    for g in range(1,nro+1):
        temp=primo(g)
        if temp==True:
            primos.append(g)
    return primos
#----------------
# arrayPrimo(13)
#---------------
def ordenPrimo(nro):
    print(len(arrayPrimo(nro)))

#--------------------
ordenPrimo(10001) 
print(arrayPrimo(10001))
#--------------------
