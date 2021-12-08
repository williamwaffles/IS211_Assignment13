

def main():
    number = int(input("Please Enter integer number: "))
    print("The 9th element of the Fibonnaci sequence is : {}".format(fibonacci(number)))
    s1 = input("Please Enter the first string: ")
    s2 = input("Please Enter the second string: ")
    print(compareTo(s1,s2))
    a=int(input("Please Enter the first integer: "))
    b=int(input("Please Enter the second integer: "))
    print("The GCD is {} ".format(gcd(a,b)))

def fibonnaci(n):

    if n == 0:
        return n

    elif n == 1 or n == 2:
        return 1

    else:
        return (fibonnaci(n - 1) + fibonnaci(n - 2))

def gcd(a, b):

    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def compareTo(s1, s2):

    if len(s1) == 0 and len(s2) == 0:
        return 0
    elif len(s1) == 0:
        return -1
    elif len(s2) == 0:
        return 1

    if s1[0] < s2[0]:
        return -1
    elif s1[0] > s2[0]:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])

if __name__ == '__main__':
    main()