# La suma de los cuadrados de los diez primeros números naturales es,
# (1^2+2^2+3^2+...+10^2+)=385
# El cuadrado de la suma de los primeros diez números naturales es,
# (1+2+3+4+...+10)^2=3025
# Por tanto, la diferencia entre la suma de los cuadrados de los diez primeros números naturales y el cuadrado de la suma es:
#  3025-385=2640
# Encuentra la diferencia entre la suma de los cuadrados de los primeros cien números naturales y el cuadrado de la suma. 
def sumaCuadrados():
    sumaCuadrados=0
    for nro in range(1,11):
        sumaCuadrados=nro**2 + sumaCuadrados
    return sumaCuadrados

def cuadradoSuma():
    cuadradoSuma=0
    for nro in range (1,11):
        cuadradoSuma=nro+cuadradoSuma
    cuadradoSuma=cuadradoSuma**2
    return cuadradoSuma
    # print (nro)
def diferencia():
    diferencia= cuadradoSuma()-sumaCuadrados()
    print(diferencia)
diferencia()