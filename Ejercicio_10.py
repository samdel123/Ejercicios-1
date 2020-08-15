#Lista de compras Articulo, Cantidad, Precio

#Agregar Articulos, Cantidad, Precio y calculo del monto a pagar
print("Agrega Items a la lista de Compras:")
item = input('Articulo: ')
Compras = []
lista = []

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
    item = input('Articulo: ')       

#Creando Lista de Articulos 
Articulos = []
for Compras in Compras:
    Articulos.append(Compras[0])

#Sacando los Artuculos Unicos
Articulos_unicos = []
Articulos_c1 = list(Articulos)
Articulos_c2 = list(Articulos)

for n in Articulos_c1:
    if n not in Articulos_unicos:
        Articulos_unicos.append(n)
    else:
        Articulos_c2.remove(n)

#Mostrando la cantidad de item y la cantidad de items sin repetir (unicos)
print("Cantidad de Item en lista:",len(Articulos))
print("Cantidad de Item sin repetir:",len(Articulos_unicos))