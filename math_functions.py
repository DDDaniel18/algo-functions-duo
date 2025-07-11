"""
ספרייה של פונקציות אלגוריתמיות
נוצר על ידי דניאל דויטש
"""

def welcome():
    print("welcome to the library")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def isPrime(n, div):
    if n < 2:
        return False
    if n % div == 0:
        return False
    if div == 1:
        return True
    return isPrime(n, div - 1)


if __name__ == "__main__":
    welcome()
    print(factorial(5))
    num = 11
    print(isPrime(num, num - 1))