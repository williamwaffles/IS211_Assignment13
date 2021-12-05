
def fibnum(n):

    if n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return (fibnum(n - 1) + fibnum(n - 2))

def GCD(a, b):

    if b == 0:
        return a
    else:
        return GCD(b, a % b)

