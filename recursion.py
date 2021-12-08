

def main():

    print("Time for some recursion! ")
    print("Let\'s start with the Fibonnaci sequence...")
    n = int(input("Please enter an integer: "))
    print(f"The {n} element of the Fibonnaci sequence is : {fibonnaci(n-1)}")

    print("Let\'s calculate the greatest common divisor!")
    a = int(input("Please enter an integer: "))
    b = int(input("Please enter another integer: "))
    print(f"You've entered {a} and {b}.")
    print(f"The GCD is {gcd(a, b)} ")

    print("Finally, let\'s compare two strings!")
    s1 = input("Please Enter the first string: ")
    s2 = input("Please Enter the second string: ")
    print(f"You've entered {s1} and {s2}.")
    print(compareTo(s1,s2))


def fibonnaci(n):

    if n == 0:
        return 0
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

    if len(s1) == 0 and len(s2) == 0 or len(s1) == len(s2):
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