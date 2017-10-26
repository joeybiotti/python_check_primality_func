def get_numbers(promt):
    '''rerturns interger value'''
    return int(input(prompt))

def num_is_prime(num):
    if num == 1:
        prime = False
    elif num == 2:
        prime == True
    else:
        prime = True
        for check_num in range(2, (num /2)+1):
            if num % check_num == 0:
                prime = False
                break
    return prime

def prime_num(number):
    prime = prime_number(num)
    if prime:
        descriptor = ""
    else:
        descriptor = "Not "
    print(num, "is ", descriptor, "a prime number. ")
