from fibonacci import fibonacci

def goldenratio_sequence(n):
    """
    This function calculates the golden ratios between the numbers in the 
    fibonacci sequence. 

    The argument that it takes is the number of fibonacci numbers that want 
    to be used to estimate the golden ratio

    The length of the list returned is 2 less than the number of fibonacci 
    numbers used
    """

    fibList = fibonacci(n)

    goldenRatio = []

    for count in range(1, n - 1):
        # Adding each of the new ratios to the end of the golden ratio list
        goldenRatio.append(fibList[count + 1] / fibList[count])

    return goldenRatio


def find_minimum_fibonacci_numbers(tolerance=0.0000000001, maxnum=100):
    """
    This function finds the minimum number of fibonacci numbers that need to 
    be used to estimate the golden ratio to within a certain tolerance

    The two arguments are the tolerance, which takes a float value, and the 
    maxnum, which takes an integer value and tells the program the maximum 
    number of fibonacci number that will be used to estimate the golden ratio
    """

    # We hard code in the actual golden ratio to compare against our estimated 
    # value
    actualGoldenRatio = 1.6180339887498948

    ratioList = goldenratio_sequence(maxnum)

    # The count starts at two because the golden ratio sequence program 
    # returns a list which has 2 less values than the number of fibonacci 
    # numbers used, therefore, we need to compensate for this
    count = 2

    for x in ratioList:
        # This for loop works out the difference between our estimated value 
        # for the golden ratio and the actual value, if it is below the 
        # tolerance then it is the value that the user wants to recieve
        count = count + 1
        if abs(x - actualGoldenRatio) <= tolerance:
            return (count), x



if __name__ == "__main__":
    print(goldenratio_sequence(20))

    numFibNums, approxGR = find_minimum_fibonacci_numbers(10**-10)
    print (numFibNums, 'numbers approximated to a tolerance of 10^-10.')
    print('The approximated value is', approxGR)

    numFibNums, approxGR = find_minimum_fibonacci_numbers(10**-14)
    print (numFibNums, 'numbers approximated to a tolerance of 10^-14.')
    print('The approximated value is', approxGR)

    numFibNums, approxGR = find_minimum_fibonacci_numbers(10**-18)
    print (numFibNums, 'numbers approximated to a tolerance of 10^-18.')
    print('The approximated value is', approxGR)