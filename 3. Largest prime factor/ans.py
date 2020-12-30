from math import sqrt

n = 4376596150763457 # Number of which we want greatest prime factor.

ans = -1 # initializing with not smallest value.

# since number we are checking factors for 
# is already odd we dont need to check even
# numbers.
# 
# since any prime factor 
for i in range(3, int(sqrt(n)) + 1, 2):
    while n % i == 0:
        ans = i
        n /= i
    
if n > 2: 
    ans = n

print(int(ans))