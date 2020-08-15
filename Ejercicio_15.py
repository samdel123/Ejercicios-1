#Lista de compras Articulo, Cantidad, Precio, Representacon Tabular, Articulo Mayor y Menor costo
import os
import csv
#Archivo a: es para añadir al archivo w: para sustituirlo
archivo = open("Lista de Compras.csv","w")

#Agregar Articulos, Cantidad, Precio y calculo del monto a pagar
print("Agrega Items a la lista de Compras:")
item = input('Articulo: ')
Compras = []
lista = []
Articulos = []
cont = 0
while item != "parar": 
    cantidad = int(input('Cantidad: '))
    precio = int(input('Precio: ')) 
    Monto = cantidad*precio
    print("Monto a Pagar:","$",Monto)
    lista.append(item)
    lista.append(cantidad)
    lista.append(precio) 
    lista.append(Monto)
    Compras.append(lista)
    lista = []
    Articulos.append(Compras[cont][0])
    cont = cont + 1
    item = input('Articulo: ')

    while item  in Articulos:
        print('!Este Articulo esta Repetido, Coloque otro distinto¡')
        item = input('Articulo: ')

#Escribiendo en archivo
ccompras = list(Compras)
archivo.write('Articulo,Cantidad,Precio,Monto\n')
for ccompras in Compras:  
    archivo.write(str(ccompras[0])+',')
    archivo.write(str(ccompras[1])+',')
    archivo.write(str(ccompras[2])+',')
    archivo.write(str(ccompras[3])+'\n')
    
#Mostrando la cantidad de item y la cantidad de items sin repetir (unicos)
print('\n')
print('{:^10} {:^10} {:^10} {:^10}'.format('Articulo', 'Cantidad', 'Precio', 'Monto a pagar\n') )
for n in Compras:
    Art = n[0]
    Cant = n[1]
    Pre	= n[2]
    Mon = n[3]
    print('{:^10} {:^10} {:^10} {:^10}'.format(Art.title(), Cant, Pre, Mon))
print('\n')
print("Cantidad de Item en lista:",len(Articulos))

#Mayor
MayorP = Compras[0]
MenorP = Compras[0]
MayorM = Compras[0]
MenorM = Compras[0]
for Compras in Compras:
    if Compras[2] > MayorP[2]: 
        MayorP = Compras
    if Compras[2] < MenorP[2]: 
        MenorP = Compras
    if Compras[3] > MayorM[3]: 
        MayorM = Compras
    if Compras[3] < MenorM[3]: 
        MenorM = Compras

print("Producto mas costoso es:",MayorP[0],MayorP[2])
print("Monto a pagar mas alto es:",MayorM[0],MayorM[3])
print("Producto mas economico es:",MenorP[0],MenorP[2])
print("Monto a pagar mas bajo es:",MenorM[0],MenorM[3])
print('\n')

archivo.close()
comprobar = os.path.isfile('Lista de Compras.csv')
if comprobar == True: 
    print('Se a guardado la lista en el fichero: Lista de Compras.csv')