#Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas, hasta que el usuario introduzca la palabra “terminar”. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
diccionario = {}
x="Terminar"
c=""
palabras = input("Introducca las palabras en español e inglés separadas por dos puntos ")
clave,valor=palabras.split(":")
diccionario[clave]=valor
c = input("Desea terminar? ")
while x!=c:
    palabras = input("Introducca las palabras en español e inglés separadas por dos puntos ")
    clave,valor=palabras.split(":")
    diccionario[clave]=valor
    c = input("Desea terminar? ")
frase= input("Introduzca una frase en castellano ")
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')