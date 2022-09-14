##Nicolás Gómez - Javiera Riveros

alfabeto = "abcdefghijklmnopqrstuvwxyz "
indexado1 = dict(zip(alfabeto, range(len(alfabeto))))
indexado2 = dict(zip(range(len(alfabeto)), alfabeto))


def encriptado(mensaje, passw):
    encriptado = ""
    mensaje_separado = [
        mensaje[i : i + len(passw)] for i in range(0, len(mensaje), len(passw))
    ]

    for separacion in mensaje_separado:
        i = 0
        for letra in separacion:
            numero = (indexado1[letra] + indexado1[passw[i]]) % len(alfabeto)
            encriptado += indexado2[numero]
            i += 1

    return encriptado

def desencriptado(cifrado, passw):
    desencriptado = ""
    encriptación_separada = [
        cifrado[i : i + len(passw)] for i in range(0, len(cifrado), len(passw))
    ]

    for separacion in encriptación_separada:
        i = 0
        for letra in separacion:
            numero = (indexado1[letra] - indexado1[passw[i]]) % len(alfabeto)
            desencriptado += indexado2[numero]
            i += 1

    return desencriptado


def main():
    
    passw = "holatodos"
    
    texto_entrada= "mensajedeentrada.txt"
    archivo = open(texto_entrada,"r")
    leer=archivo.read()
        
    mensaje_original=leer.lower()
    mensajehash=hash(leer)

    cifrado1=encriptado(mensaje_original,passw)
    cifrado2=encriptado(cifrado1,passw)

    texto_cifrado = "mensajeseguro.txt"
    archivo1= open(texto_cifrado,"w+")
    archivo1.write(cifrado2)
    archivo1.close()
    
    archivo2 = open("mensajeseguro.txt")
    leer2=archivo2.read()

    decifrado1=desencriptado(leer2, passw)
    decifrado2=desencriptado(decifrado1, passw)

    decifradohash=hash(decifrado2)

main()
