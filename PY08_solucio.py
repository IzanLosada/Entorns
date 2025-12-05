contador = 0   # variable global

def sumar(x):
    global contador
    contador = x + 1 
    return contador

sumar(5)

print(contador)   # Result won't modify global variable
