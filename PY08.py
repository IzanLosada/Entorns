number = 0   # Global variable

def add(x):
    number = x + 1 
    return number

add(5)
print(number)   # Result won't modify global variable

