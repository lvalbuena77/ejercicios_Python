## Función para determinar si un número es primo o no
## Código: Python 3.6.1
def es_primo(numero): 
    if numero == 1: 
        print("El numero 1 no es primo")
        return False
        
    for i in range(2, numero): 
        if numero % i == 0: 
            print("El numero: ", numero, "no es primo.", i, "es divisor")
            return False
    print("El numero: ", numero, "es primo")        
    return True
    


print(es_primo(2))
