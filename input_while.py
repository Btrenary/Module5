"""
Author: Brady Trenary
Program: input_while.py

Prompts user for numeric input between 1 and 100. prompt until the input is in correct range
"""


if __name__ == '__main__':

    #declare list variable
    my_list = []

    #prompt and get user input
    my_input = float(input("Enter a number between 1 and 100 (-1 to exit):"))

    #while loop using sentinel value
    while my_input != -1:

        #while input not good (in range)
        while my_input <1 or my_input > 100:
            #prompt user for good input
            my_input = float(input("Enter a number between 1 and 100:"))
        #store in list
        my_list.append(my_input)
        # prompt user for good input
        my_input = float(input("Enter a number between 1 and 100:"))

    #print input list
    print(my_list)
