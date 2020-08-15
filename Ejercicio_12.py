#Lista de compras Articulo, Cantidad, Precio y Representacon Tabular

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