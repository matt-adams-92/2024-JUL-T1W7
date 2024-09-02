# return statement - returns a value from a function

# 4 + 5 - 2

def add(num1, num2):
    sum = num1 + num2
    return sum


def subtract(num1, num2):
    difference = num1 - num2
    return difference

partial_calculated_value = add(4, 5)
final_result = subtract(partial_calculated_value, 2)

print(final_result)