# Write a program to print the first n numbers of a Fibonacci sequence
# Fibonacci sequence of size 6 is { 0, 1, 1, 2, 3, 5} where n is 6


def fibonacci_sequence_generator(num):
    if type(num) != int:
        return "Incorrect datatype"
    
    fibonacci_sequence = []
    if num < 0 : # negative
        return "Incorrect value"
    elif num == 0 :
         return fibonacci_sequence
    elif num == 1 :
        fibonacci_sequence.append(0)
    else:
        # add to the fibonacci sequence list
        fibonacci_sequence.append(0)
        fibonacci_sequence.append(1)
        while(len(fibonacci_sequence) < num):
                fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        
    return fibonacci_sequence

if __name__ == "__main__":
     print(fibonacci_sequence_generator(200))