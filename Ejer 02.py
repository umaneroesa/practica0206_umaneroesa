#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje “<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>”.
diccionario ={}
diccionario["Nombre"] = input("Dime tu nombre ")
diccionario["edad"] = input("Dime tu edad ")
diccionario["direccion"] = input("Dime tu direccion ")
diccionario["telefono"] = input("Dime tu telefono ")
print(diccionario['Nombre'], 'tiene', diccionario['edad'], 'años, vive en', diccionario['direccion'], 'y su número de teléfono es', diccionario['telefono'])