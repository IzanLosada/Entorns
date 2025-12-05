# Infinte recursion
def countdown(n):
    print(n)
    if n == 0:
        return
    return countdown(n - 1)

countdown(3)

