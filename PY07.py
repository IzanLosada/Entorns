# Infinite recursion
def countdown(n):
    print(n)
    return countdown(n - 1)   # No base condition


countdown(3)
