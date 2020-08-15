import csv
archivo = open("Lista de Compras.csv")
leer = archivo.readlines()
leerc = list(leer)
archivo.close()
Compras = []
Articulos = {}
cont = 0
for leer in leerc:
    Dic = leer.split(',')
    Articulos[Dic[cont]] = Dic[1:]

encabezado = 'Articulo'
del Articulos[encabezado]
Compras.append(Articulos)

def Buscar():
    Palabra = input('Escriba el articulo que quiere buscar: ').lower()
    
    if Palabra in Articulos:
        consulta = Articulos.get(Palabra) 
        Diccionario = {'Articulo':Palabra, 'Cantidad':int(consulta[0]), 'Precio':int(consulta[1]), 'Monto':int(consulta[2]) }
        print (Diccionario)
    else:
        print('Este Articulo no esta en la Lista')

def Agregar():

    print("Agregar Articulo: ")
    Articulo = input('Articulo: ').lower()
    while True:
        if Articulo in Articulos:
            print('!Este Articulo esta en la lista, Coloque otro distinto¡')
            Articulo = input('Articulo: ').lower()
        else:         
            Cantidad = int(input('cantidad: '))
            Precio = int(input('Precio: '))
            Monto = Cantidad * Precio  
            break 
            
    Articulos[Articulo] = [Cantidad, Precio, Monto] 
    print('Su Articulo Fue Agregado\n' ,Articulos)

def Eliminar():
    Articulo = input('Ingrese el articulo que desea Borrar: ').lower()
    while True:
        if Articulo in Articulos:
            del Articulos[Articulo]
            print('El Articulo fue Eliminado')
            break
        else:
            print('Este Articulo no esta en la lista')    
            break   

def Guardar():
    archivo = open("Lista de Compras.csv","w")
    archivo.write('Articulo,Cantidad,Precio,Monto\n')
    claves = list(Articulos.keys())
    cclaves= len(claves)
    cont = 0  

    while True:
        if cont == cclaves:
            break
        else:
            clv = claves[cont]
            archivo.write(str(clv)+',')
            archivo.write(str(Articulos[clv][0])+',')
            archivo.write(str(Articulos[clv][1])+',')
            archivo.write(str(Articulos[clv][2])+'\n')
            cont = cont + 1   
    archivo.close()    
    print('Su Archivo fue modificado')

while True:
    print('Seleccione la accion que desea realizar:\n','B = Escriba B para Buscar un articulo en la lista\n',
    'A = Escriba A para Agregar un articulo en la lista\n', 'E = Escriba E para Eliminar un articulo en la lista\n',
    'G = Escriba G para Guardar Cambios en el archivo\n', 'S = Para terminar\n')

    Funcion = input('Que Accion desea Realizar: ').upper()

    if Funcion == 'B':
        Buscar() 
        print('\n')
    elif Funcion == 'A':
        Agregar()
        print('\n')
    elif Funcion == 'E':
        Eliminar()
        print('\n')
    elif Funcion == 'G': 
        Guardar()
        print('\n')
    elif Funcion == 'S':    
        break