def divisores(nro):
    listDiv=[]
    for i in range(1,nro+1):
        if nro%i==0:
            listDiv.append(i)
    return listDiv
def divisoresSuma(nro):
    x=0
    suma=0
    while x<nro:
        x+=1
        suma=suma+x
    return suma, divisores(suma)
def limiteDivisores(nro):
    i=0
    while i >=0:
        i+=1
        if int(len(divisoresSuma(i)[1]))>nro:
            return f"el numero es: {i} \nsecuencia de numero triangular: {divisoresSuma(i)[0]} \nla cantidad de divisores son : {nro}\nsus divisores son: {divisoresSuma(i)[1]}"
print(limiteDivisores(200))