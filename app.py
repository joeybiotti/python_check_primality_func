def prime_num():
    x = int(input("Your number is: "))
    for i in range(2, round(x/2)+ 2):
        if x % i == 0:
            print("Not a prime number.")
            break
        else:
            print("This is a prime number")
            break

prime_num()
