n = 100

# Formula for sum of squares of first n natural numbers.
# n^3 / 3 + n^2 / 2 + n / 6 
sum_of_sq = ((n**3)/3) + ((n**2)/2) + (n/6)

# square of sum of first n natural numbers.
# (n(n+1) / 2)^2 
sq_of_sum = (n*(n+1)/2)**2

print(abs(sq_of_sum - sum_of_sq))