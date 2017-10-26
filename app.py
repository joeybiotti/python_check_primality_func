def prime_num():
    i = int(input("Your number is:\n"))
    for x in range(2, round(x/2)+ 2):
        if x % i == 0:
            print("Not a prime number.")
            break
        else:
            print("This is a prime number")
            break

prime_num()
