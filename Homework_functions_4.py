def sumofdigits(number):
    sum = 0
    for _ in range(len(str(number))):
        digit = number%10
        sum = sum + digit
        number = number//10
    return(sum)

print(sumofdigits(4670))
