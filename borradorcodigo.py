with open("data.csv", "r") as file:
        list_data = file.readlines()    

suma = 0

for values in list_data:
    values_tmp = values.split()
    suma += int(values_tmp[1])

print(suma)