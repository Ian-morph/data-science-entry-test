def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if str(num).isnumeric() and str(divisor).isnumeric():
        status = (num % divisor == 0)
        print(status)
        return(status)
    else:
        print("number is not numeric")


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

check_divisibility(10, 2)
check_divisibility(7, 3)