"""This module contains program to check if pairs of strings are anagram."""

def check_total_comparisons_validity(total_comparisons_param):
    """Function to validate if the total number of comparisons is a valid input"""
    try:
        total_comparisons = int(total_comparisons_param)
        if total_comparisons < 0 or (float(total_comparisons_param)%1) != 0:
            return 0
        return 1
    except: # pylint: disable=bare-except
        return 0

def get_total_number_of_comparisons():
    """Function to read the input of end user for the total number of String sets.
    returns - total number of comparisons to be done - Integer"""
    is_valid_total_comparisons = 1
    total_comparisons = input("Enter the number of comparisons to be done:- ")
    is_valid_total_comparisons = check_total_comparisons_validity(total_comparisons)
    if is_valid_total_comparisons == 0:
        print("Error: Entered value should be a positive integer")
    while is_valid_total_comparisons == 0:
        total_comparisons = input("Enter the number of comparisons to be done:- ")
        is_valid_total_comparisons = check_total_comparisons_validity(total_comparisons)
        if is_valid_total_comparisons == 0:
            print("Error: Entered value should be a positive integer")
    return int(total_comparisons)

def get_string_sets_input(total_comparisons):
    """Function to read the end user input for String1 of set i and String2 of set i
    returns - List of Lists - Inner lists - [string1, string2]"""
    print("Enter the String sets for comparisons:- ")
    string_sets_list = []
    for i in range(total_comparisons):
        string_set = []
        string_set.append(input("Enter String 1 for set " + str(i+1) + ":- "))
        string_set.append(input("Enter String 2 for set " + str(i+1) + ":- "))
        string_sets_list.append(string_set)
    return string_sets_list

def compare_lengths(string1, string2):
    """Fucntion to compare lengths of two strings
    returns 0, if lengths are different, returns 1, if lenghts are equal"""
    if len(string1) == len(string2):
        return 1
    return 0

def check_char_frequencies(string1, string2):
    """Function to check if frequencies of every character in string1 matches the frequency
    of corresponding character in string2
    Returns 1 if all frequency of every character in string1 matches its frequency in string2
    and if both the strings have same set of characters"""
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
    for key in map1.keys():
        if key in map2.keys():
            if map1[key] != map2[key]:
                return 0
        else:
            return 0
    return 1

def check_anagram(string_set):
    """function to check the base case i.e. if lenghts of strings are equal
    calls function to check if the given strings have same frequencies of all characters
    returns the result accordingly"""
    string1 = string_set[0]
    string2 = string_set[1]
    string1_formatted = "".join(string1.split(" "))
    string2_formatted = "".join(string2.split(" "))
    is_length_equal = compare_lengths(string1_formatted, string2_formatted)
    if is_length_equal == 0:
        return 0
    return check_char_frequencies(string1, string2)

if __name__ == "__main__":
    total_comparisons = get_total_number_of_comparisons()

    string_sets_list = get_string_sets_input(total_comparisons)

    for i in range(len(string_sets_list)):
        is_anagram = check_anagram(string_sets_list[i])
        if is_anagram == 0:
            print(string_sets_list[i][0] + " & " + string_sets_list[i][1] + " are not Anagrams")
        else:
            print(string_sets_list[i][0] + " & " + string_sets_list[i][1] + " are Anagrams")
