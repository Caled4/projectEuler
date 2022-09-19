# La suma de los números primos por debajo de 10 es 2 + 3 + 5 + 7 = 17.
# Encuentra la suma de todos los números primos por debajo de dos millones
def div(nro):
    h=0
    while h < nro:
        h+=1
        if h !=1 and h!= nro:
            if nro%h==0:
                return True
def primo(g):
    if div(g)==True:
        return False
    else:
        return True
# primo(67)
def sumaList(temp):
    suma=0
    for idx in range(int(len(temp))):
        suma=suma+temp[idx]
    print(suma)
# sumaList([4,8,6])
def limite(lim):
    listPrimo=[]
    suma=0
    for f in range(1,lim+1):
        # print(f)
        # print(primo(f))
        if primo(f)==True:
            # suma=suma+f
            listPrimo.append(f)
    print(listPrimo)
    sumaList(listPrimo)

limite(20)