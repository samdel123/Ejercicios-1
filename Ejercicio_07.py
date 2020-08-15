#Lista de Compras

def lista():
    Compras=[]
    item = input('Escriba los elementos de su lista de compras:\n').lower()
    while item != "parar":
        Compras.append(item)
        item = input().lower()    
    print("Cantidad de Item en lista:",len(Compras))

lista()
