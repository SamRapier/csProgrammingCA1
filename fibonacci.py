def fibonacci(n):
    """
    This function calculates the fibonacci numbers and saves them in a list

    The argument that is taken is the number of fibonacci numbers to be 
    calculated
    """
    if n < 2:
        F = 'n must be greater than or equal to 2'
    else:
        # The first two fibonacci numbers are initialised into the list so that 
        # the rest can be calculated
        F = [0 ,1]
        for count in range(2, n):
            F.append(F[count-1] + F[count-2])
        
    return F


if __name__ == "__main__":
    print(fibonacci(20))
    print(fibonacci(1))