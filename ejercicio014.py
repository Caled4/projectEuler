def susecion(nro):
    rpta=[]
    while nro !=1:
        if nro%2==0:
            rpta.append(nro)
            nro=nro/2            
        else:
            rpta.append(nro)
            nro=3*nro+1
    rpta.append(nro)            
    return  int(len(rpta)),rpta
# print(susecion(13))
def susecionLarga(limite):
    rpta=1
    for i in range(1,limite+1):
        if susecion(i)[0]>rpta:
            rpta=susecion(i)[0]
    return f"cantidad de eslavones {susecion(i)[0]}\nel numero es: {susecion(i)[1][0]}\nla secuencia es: {susecion(i)[1]}"
print(susecionLarga(1000000))