def fibonacci(n):
    """
    מחזירה את n המספרים הראשונים בסדרת פיבונאצ'י
    """
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq