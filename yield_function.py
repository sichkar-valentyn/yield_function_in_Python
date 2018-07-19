# File: yield_function.py
# Description: Function for modifying lists with remove and count methods
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Using yield instead of return in functions in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/yield_function_in_Python (date of access: XX.XX.XXXX)




# Implementing the task
# Show n first numbers of the sequence
# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 etc.


# Creating a function with the feature of generator to generate a sequence
def generator(n):
    # Setting the variable to control the number of output integers in the sequence
    count = 0
    # Going through given sequence from '1' to 'n + 1' and break when it's reached 'n' output integers
    for i in range(1, n + 1):
        # Generating sequence of 'i' times repeated integers of 'i'
        for j in range(i):
            # Creating a rule to break when sequence is a size of 'n'
            count += 1
            if count > n:
                return  # It is also possible to write here 'break'
            # Generating numbers of the sequence as string variables
            # By using 'yield' generator-function will remember where it was previous time
            yield str(i)


# Showing the results by joining generated integer numbers as string values
print(' '.join(generator(6)))

