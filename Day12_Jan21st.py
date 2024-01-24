# Write a program to reverse a given string

def reverse_string(input_string):
    if type(input_string) != str :
        return "Incorrect datatype"
    else:
        print("Input string is {}".format(input_string))
        return input_string[-1::-1]