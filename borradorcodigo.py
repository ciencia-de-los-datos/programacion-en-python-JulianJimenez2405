with open("data.csv", "r") as file:
        lista_datos = file.readlines()    

suma = 0

for valores in lista_datos:
    valores_temporales = valores.split()
    suma += int(valores_temporales[1])

print(suma)