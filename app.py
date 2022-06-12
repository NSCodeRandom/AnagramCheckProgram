# Function to validate if the total number of comparisons specified by end user is a valid input
# returns 1 if it is a valid input else returns 0
def checkTotalComparisonsValidity(totalComparisonsParam):
    try:
        totalComparisons = int(totalComparisonsParam)
        if totalComparisons < 0 or (float(totalComparisonsParam)%1) != 0:
            return 0
        return 1
    except:
        return 0  
    
# Function to read the input of end user for the total number of String sets end user want to supply for comparison
# returns - total number of comparisons to be done - Integer
def getTotalNumberOfComparisons():
    isValidTotalComparisons = 1
    totalComparisons = input("Enter the number of comparisons to be done:- ")
    isValidTotalComparisons = checkTotalComparisonsValidity(totalComparisons)
    if isValidTotalComparisons == 0:
        print("Error: Entered value should be a positive integer")
    while isValidTotalComparisons == 0:
        totalComparisons = input("Enter the number of comparisons to be done:- ")
        isValidTotalComparisons = checkTotalComparisonsValidity(totalComparisons)
        if isValidTotalComparisons == 0:
            print("Error: Entered value should be a positive integer")
    return int(totalComparisons)

# Function to read the end user input for String1 of set i and String2 of seti
# returns - List of Lists - Inner lists - [string1, string2]
def getStringSetsInput(totalComparisons):
    print("Enter the String sets for comparisons:- ")
    stringSetsList = []
    for i in range(totalComparisons):
        stringSet = []
        stringSet.append(input("Enter String 1 for set " + str(i+1) + ":- "))
        stringSet.append(input("Enter String 2 for set " + str(i+1) + ":- "))
        
        stringSetsList.append(stringSet)
    return stringSetsList

# Fucntion to compare lengths of two strings
# returns 0, if lengths are different, returns 1, if lenghts are equal
def compareLengths(string1, string2):
    if len(string1) == len(string2):
        return 1
    return 0

# Function to check if frequencies of every character in string1 matches the frequency of corresponding character in string2 
# Returns 1 if all frequency of every character in string1 matches its frequency in string2 and if both the strings have same set of characters
def checkCharFrequencies(string1, string2):
    string1 = "".join(string1.split(" ")).upper()
    string2 = "".join(string2.split(" ")).upper()
    map1 = {}
    map2 = {}
    for i in range(len(string1)):
        if string1[i] not in map1.keys():
            map1[string1[i]] = 1
        else:
            map1[string1[i]] += 1
        if string2[i] not in map2.keys():
            map2[string2[i]] = 1
        else:
            map2[string2[i]] += 1
    tmp = 1      
    for key in map1.keys():
        if key in map2.keys():
            if map1[key] != map2[key]:
                return 0
        else:
            return 0
        
    return 1

# function to check the base case i.e. if lenghts of strings are equal
# calls function to check if the given strings have same frequencies of all characters
# returns the result accordinglye
def checkAnagram(stringSet):
    string1 = stringSet[0]
    string2 = stringSet[1]
    string1Formatted = "".join(string1.split(" "))
    string2Formatted = "".join(string2.split(" "))
    isLengthEqual = compareLengths(string1Formatted, string2Formatted)
    if isLengthEqual == 0:
        return 0
    return checkCharFrequencies(string1, string2)

    
if __name__ == "__main__":
    totalComparisons = getTotalNumberOfComparisons()

    stringSetsList = getStringSetsInput(totalComparisons)

    for i in range(len(stringSetsList)):
        isAnagram = checkAnagram(stringSetsList[i])
        if isAnagram == 0:
            print(stringSetsList[i][0] + " & " + stringSetsList[i][1] + " are not Anagrams")
        else:
            print(stringSetsList[i][0] + " & " + stringSetsList[i][1] + " are Anagrams")
    




        
    
