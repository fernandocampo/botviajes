seguir="Si" or "S"
Vip = "Si" or "S"

while (seguir=="S" or seguir =="Si"):
    millas = int(input("Ingrese la cantidad de millas que tiene: "))
    if(millas < 150):
        print("Podes viajar a Colonia, Uruguay")
    elif(2000 < millas < 3000):
        print("Podes viajar a Lima, Peru")
    elif(millas > 3000):
        print("Podes viajar a Frankfurt, Alemania")  
    if(millas > 3000 and Vip == "Si"):
        Vip = str(input("Sos un usuario VIP? Si/No ")) 
        print("Podes viajar a Tokyo, Japon")
    seguir= input("Otra consulta? (Si/No)")
print("Gracias por consultar.")
