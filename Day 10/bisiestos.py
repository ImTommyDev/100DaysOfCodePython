def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# Pruebas
print(is_leap_year(2400))  # True
print(is_leap_year(1989))  # False
print(is_leap_year(2000))  # True
print(is_leap_year(2100))  # False
