# Holds final answer
ans = 0


# iterating from 1 to 1000 and if
# number is divisible by 3 or 5
# adding it to "ans"
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        ans += i

print(ans)