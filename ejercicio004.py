# Un número palindrómico se lee igual en ambos sentidos. El palíndromo más grande hecho del producto de dos números de 2 dígitos es 9009 = 91 × 99.
# Encuentra el palíndromo más grande hecho del producto de dos números de 3 dígitos.
def producto():
    for numero1 in range (100,1000):
        for numero2 in range(100,1000):
            producto=numero1*numero2
            if palindromo(producto) is True:
                # print(f"el primer numero es: {numero1} el segundo numero es :  {numero2}")
                rpta=producto
                nro1=numero1
                nro2=numero2
    return print(f"la respuesta es: {rpta} producto de {nro1} y {nro2}")
    
    
def palindromo(numero):
    numero=numero
    # revNumero=[]
    listNumero = list(str(numero))
    numero=list(str(numero))
    listNumero.reverse()
    if numero == listNumero:
        return True
    else:
        return False
producto()