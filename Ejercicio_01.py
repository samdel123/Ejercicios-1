#Numero de Palabras de una Cadena de Caracteres

def contar ():
    Texto = input('Ingrese una cadena de caracteres:\n')
    Texto_Separado = Texto.split()
    print('El Numero de palabras es:',len(Texto_Separado)) 
    
contar()

