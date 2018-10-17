from reverse import print_reverse

def read_words(filename):
    """
    This function opens a file, reads it and then puts the contents of the file
    into a list

    The single argument is the name of the file
    """
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines
    
def longest(words):
    """
    This function finds and prints the first longest word in a list 
    The single argument is a list
    """
    longestLength = 0
    for counter in range(len(words)):
        # We are removing the new line part off of the end of the current word 
        # and saving the result in our variable
        currentWord = words[counter].strip()

        if len(currentWord) > longestLength:
            longestWord = currentWord
            longestLength = len(currentWord)
    
    return longestWord, longestLength
    

def all_longest(words):
    """
    This funciton finds and prints a list of all the longest words in a list 
    of words

    The single argument is a list
    """
    longestLength = 0
    longestWords = []

    for counter in range(len(words)):
        # We are removing the new line part off of the end of the current word 
        # and saving the result in our variable
        currentWord = words[counter].strip('\n')

        if len(currentWord) > longestLength:
            # If it is a new longest word, we clear the list of longest words 
            # and add the new word to the end of the list
            longestWords.clear()

            longestWords.append(currentWord)
            longestLength = len(currentWord)
        elif len(currentWord) == longestLength:
            # If the current word is the same length as the longest word, we 
            # add the current word to the list of longest words
            longestWords.append(currentWord)
        
        
    print(longestWords)


if __name__ == "__main__":
    longW, longL = longest(read_words('words.txt'))
    print('longest word in the file:', longW, 'it has a length of', longL)

    all_longest(read_words('words.txt'))

    print_reverse(longW)