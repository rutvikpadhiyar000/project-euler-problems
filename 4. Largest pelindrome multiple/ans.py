
# Seems to work faster than pure mathematicle implementation.
def reverse(num):
    """ Function to reverse the number."""
    num_str = str(num)
    num_str_rev = num_str[::-1]
    return int(num_str_rev)

# Same function using mathematicle operations.
'''def reverse(num):
    """ Function to reverse the number"""
    rev = 0
    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num //= 10
'''

max = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        mul = i*j
        if mul == reverse(mul) and mul > max:
            max = mul

print(max)