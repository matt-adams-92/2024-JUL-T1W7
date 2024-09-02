# 5! = 5 * 4 * 3 * 2 * 1 = 120

# Input number as num form user
num = int(input("Enter a number: "))

# initialize i = 1
i = 1

# loop until 1 <= num
fact = 1

# loop until 1 <= num
while i <= num:
    # fact = fact * i
    fact *= i
    # i = i + 1
    i += 1

# display fact
print(fact)