def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    idx = 0
    status = False
    while idx < len(lst):
        if lst[idx] < 0:
            print(lst[idx])
            status = True
            return lst[idx]
            break
        else:
            idx += 1
    if status == False:
        print("No negatives")
        return("No negatives")
    return


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

find_first_negative([3, 5, -1, 7, -2, 8])
find_first_negative([2, 10, 7, 0])