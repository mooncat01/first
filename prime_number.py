def is_prime_number(y):
    for num in range(2, y):
        if y % num == 0:
            print("The number {num1} is not a prime number.".format(num1=y))
            return
    print("The number {num1} is a prime number.".format(num1=y))

