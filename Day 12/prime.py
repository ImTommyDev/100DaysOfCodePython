def is_prime(num):
    for n in range(1,num):
        #si el numero es divisible por un numero que no sea 1 o el mismo, no es primo
        if num % n == 0 and n != 1 and n != num:
            return False
    return True

print(is_prime(7)) # True
print(is_prime(8)) # False