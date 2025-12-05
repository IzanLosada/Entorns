# Codi recursió infinita
def cuenta_atras(n):
    print(n)
    if n == 0:
        return
    return cuenta_atras(n - 1)

cuenta_atras(3)
