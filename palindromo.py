palabra = input("Introduce una palabra: ")
print("La palabra introducida es: ", palabra)
print("La palabra al reves es: ", palabra[::-1])
if palabra == palabra[::-1]:
    print("La palabra es un palindromo")
else:
    print("La palabra no es un palindromo")

    