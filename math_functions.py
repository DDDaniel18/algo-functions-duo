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
        reutrn n * factorial(n - 1)
if __name__ == "__main__":
    welcome()
    print(factorial(5))