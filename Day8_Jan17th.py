# Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it

def string_upper_lower_count(string):
    # check if parameter passed is of string type

    if isinstance(string, str):

        upper_characters = 0
        lower_characters = 0

        for character in string:
            if character.isupper():
                upper_characters += 1
            elif character.islower():
                lower_characters += 1
            else:
                pass
        
        print("Number of upper case characters in the string {} is {} \n Number of lower case characters in the string is {}".format(string, upper_characters, lower_characters))
    else:
        print("Parameter passed {} is not of string type".format(string))
    return (upper_characters,lower_characters)