contador = 0   # variable global

def sumar(x):
    global contador
    contador = x + 1 
    return contador

sumar(5)
print(contador)   # Serà 0 no es modifica de la manera esperada