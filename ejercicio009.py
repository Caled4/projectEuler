# a < b < c
# a^2+b^2=c^2
# a + b + c = 1000.
# abc=?
#-----------------------
#--------- triple pitagorico
def triplePitagorico(a,b):
    a=a
    b=b
    rpta=(a**2)+(b**2)
    return rpta
# print(triplePitagorico(3,4))
#------ 
def hallaNumeros(y):
    #valor a
    for a in range(1,y):
        #valor b, b>a
        for b in range(a,y):
            if b>a:
                # valor de c,  c>b>a
                for c in range(b,y):
                    if c>b :
                        
                        if a+b+c==y:
                            if triplePitagorico(a,b)== c**2:
                                print(f"numero ingresado: {y}")
                                print(f"los numeros son: {a,b,c}")
                                print(f"el producto de los numeros es {a*b*c}")

#----------psdt: el digo si funciona pero demora un poco en calcular
        
hallaNumeros(1000)

