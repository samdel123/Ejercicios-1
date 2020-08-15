#Palindromo de una palabra 

def Palindromo():
    Palabra1 = input('Ingrese una palabra:\n').lower()
    Palabra2 = input('Ingrese su palindromo:\n').lower()
    Reverso = Palabra1[::-1]
    
    if Reverso == Palabra2:
        print(Palabra1,'Es Palindromo de:', Palabra2)
    else:
        print(Palabra1,'No es Palindromo de:', Palabra2)

Palindromo()