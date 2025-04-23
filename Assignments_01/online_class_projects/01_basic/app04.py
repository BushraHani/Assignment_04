#04_random_numbers

import random

# Print 10 random numbers between 1 and 100
for i in range(10):
    value = random.randint(1, 100)
    print(value, end=' ')
