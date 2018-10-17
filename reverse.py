def print_reverse(text, print_spaces=False):
    """
    This is a function which prints out a string in reverse order

    The first argument is a string, the second argument is a boolean which 
    determines if there are spaces added to the beginning of the each line when
    the string is printed out.
    """    

    stopPoint = -len(text) -1
    count = len(text) - 1

    # This for loop is going backwards starting at -1 so that the string 
    # is read from the end and eventually reaches the beginning
    for counter in range(-1, stopPoint, -1):   

        #This if statement adds the spaces in front of each letter if 
        # print_spaces is true 
        if print_spaces == True:
            startChar = " " * count
        else:
            startChar = ""
        count = count -1

        print(startChar + text[counter])



if __name__ == "__main__":
    print('Without Spaces:')
    print_reverse('reversestring', False)

    print('With Spaces:')
    print_reverse('reversestring', True)