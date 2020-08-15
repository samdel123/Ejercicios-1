#Lista de Compras Elementos Unicos 

#Agregar items a la lista de compras
def lista():    
    Compras=[]
    item = input()
    while item != "parar":
        Compras.append(item)
        item = input()

    #Sacando los Items Unicos de la lista de Compras    
    unicos = []
    compras_copia1 = list(Compras)
    compras_copia2 = list(Compras)
    
    for n in compras_copia1:
        if n not in unicos:
            unicos.append(n)
        else:
            compras_copia2.remove(n)

    #Mostrando Resultados de cantidad de item mas la cantidad de item que se repiten o (unicos)
    print("Cantidad de Item en lista:",len(Compras))
    print("Cantidad de Item sin repetir:",len(unicos))

lista()