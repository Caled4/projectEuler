# Un número palindrómico se lee igual en ambos sentidos. El palíndromo más grande hecho del producto de dos números de 2 dígitos es 9009 = 91 × 99.
# Encuentra el palíndromo más grande hecho del producto de dos números de 3 dígitos.
# for numero1 in range(1,10):
#     for numero2 in range(1,10):
#         palindromo=numero1*numero2
#         print(palindromo) 
#         # if palindromo==
def revertirNumero():
 
    n=4948

    strNumero= str(n)
    idx= len(strNumero)-1
    reverso=[]
    # reverso.append(n)
    while (idx >= 0):
      reverso.append(strNumero[idx])
      idx = idx - 1

    print(reverso)

    
revertirNumero()