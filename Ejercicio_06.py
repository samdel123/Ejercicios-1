#Hostname de una URL
url = "www.google.com"


def Host (enlace):
    separa = enlace.split('.')
    print("el Hostname es:",separa[2])


Host(url)