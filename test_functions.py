# בדיקות פשוטות באמצעות assert
from functions import factorial, isPrime
from fibonacci import fibonacci
from sorting import bubble_sort, quick_sort

# בדיקת factorial
assert factorial(0) == 1
assert factorial(5) == 120

# בדיקת isPrime
assert isPrime(2, 1)
assert not isPrime(4, 3)

# בדיקת fibonacci
assert fibonacci(5) == [0, 1, 1, 2, 3]

# בדיקות מיון
assert bubble_sort([3, 1, 2]) == [1, 2, 3]
assert quick_sort([3, 1, 2]) == [1, 2, 3]

print("כל הבדיקות עברו בהצלחה!")
