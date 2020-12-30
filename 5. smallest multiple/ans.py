def gcd(num1, num2):
    """Find greatest common divisor of given numbers"""

    gcd = 1
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    return gcd

# If number is not divisible by multiplication
# till now than multiply greatest common
# divisor to 'mul' 
mul = 1
for i in range(2, 21):
    mul = int(mul)
    if mul % i != 0:
        mul *= i / gcd(mul, i)

print(mul)