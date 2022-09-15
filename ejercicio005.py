# 2520 es el número más pequeño que se puede dividir por cada uno de los números del 1 al 10 sin resto.
# ¿Cuál es el número positivo más pequeño que es divisible por todos los números del 1 al 20?
# from sqlite3 import adapt
def divisores(numero):
    numero=numero
    rpta=[]
    for div in range(1,11):
        
        if numero%div==0:
            rpta.append(div)
            if len(rpta)==10:
                return True
    # print(rpta)
def hallarNumero():
    i=1
    while divisores(i)!=True:
        i+=1
    print(i)
# NOTA-----------------> al colocar los valores para que sea dibisible por los 20 digitos la compilacion demora mucho por que a partir del 8 digito el resultado mostrado deja de ser casi intantanea porque cada cifra incrementa la dificultad de mane exponencial
hallarNumero() 