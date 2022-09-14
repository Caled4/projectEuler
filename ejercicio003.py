# Los factores primos de 13195 son 5, 7, 13 y 29.
# ¿Cuál es el mayor factor primo del número 600851475143?
#----------------------------------------------------------
# numero=600851475143
factorMayor =0
def factorPrimo():
    for numero in range(2,13195):
        # print(numero)
        if 13195 % numero == 0:
            if numero%numero ==0 :
                factorMayor=numero
    print(factorMayor)
    
    # print("el mayor factor primo es: "+numero)
# def mayorFactorPrimo ():
#     factorPrimo()

def primo(num):
    for n in range(2, num):
        if num % n == 0:
            # print("No es primo", n, "es divisor")
            return False
    # print("Es primo")
    return True
# mayorFactorPrimo()
factorPrimo()