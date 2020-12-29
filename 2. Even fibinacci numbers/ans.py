# We can observe that every 3rd term is even.
# and given two condecutive even terms a and b
# respectively next even term will be 4b + a 

# Initializing series with first two even terms
a, b = 2, 8

# initializing "ans" with value of first even term.
ans = 2

# adding all even terms till 4 million.
while b <= 4000000:
    a, b = b, 4*b + a
    ans += a

print(ans)