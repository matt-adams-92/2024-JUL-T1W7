# Input numerator as n and denominator as d
n = int(input("Enter the numerator: "))
d = int(input("Enter the denominator: "))

# If d is 0
if d == 0:
    # display "denominator cannot be zero"
    print("Denominator cannot be zero")

# else
else:
    # calculate q = n / d
    q = n / d
    # display q
    print(q)