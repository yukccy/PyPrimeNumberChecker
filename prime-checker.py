n = int(input("Check this number: "))

def prime_checker(number):
    num_of_divisor = 1
    divisor = 2
    count = 1
    while num_of_divisor == 1 and count != number:
        if number == divisor:
            num_of_divisor = 1
        elif number % divisor == 0:
            num_of_divisor += 1
        else:
            divisor += 1
        count += 1
    if num_of_divisor == 1:
        print("It is a prime number")
    else:
        print("It is not a prime number")

prime_checker(number=n)