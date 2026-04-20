def is_armstrong_number(number):
    
    digits_nbr = str(number)
    length = len(digits_nbr)
    total = 0

    for n in digits_nbr:
        total += int(n) ** length

    return total == number

