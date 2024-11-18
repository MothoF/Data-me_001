# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    if lst:
        return lst[::-1]
    else:
        return lst  # Implement this

def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    #element_count = 0
    #for element in lst:
    if lst:
        element_count = lst.count(element)
        return element_count 
    else:
        return 0 # Implement this

def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    if dct:
        list_of_keys = []
        for key in dct.keys():
            if dct[key] == value:
                list_of_keys.append(key) 
        return list_of_keys 
    else:
        return [] # Implement this

def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    return sorted(lst1+lst2)  # Implement this

def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """#git@github.com:MothoF/Data-me_001.git
    list_length = len(numbers)
    n = 0
    viable = False
    while n<list_length:
        try:
            if numbers[n+1] == numbers[n]:
                viable = False
            else:
                viable = True
        except IndexError:
            pass
        n+=1
    if viable == True:
        max_number = max(numbers)
        numbers.remove(max_number)
        return max(numbers) 
    else:
        return None # Implement this

def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    str1_list = list(str1)
    str2_list = list(str2) 
    return sorted(str1_list) == sorted(str2_list) # Implement this


def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    flat_list = []
    for list in nested_list:
        for item in list:
            flat_list.append(item)
    return flat_list # Implement this


def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    st = set(lst)
    return list(st) # Implement this

def find_common_elements(lst1, lst2):
    """
    Finds common elementgit@github.com:MothoF/Data-me_001.gits between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    common_elements = []
    for item in lst1:
        if item in lst2:
            common_elements.append(item)
    return common_elements # Implement this

#list = [0,1,3,5,4,89,4,85]
#print(find_common_elements([], [1, 2]))
#print(reverse_list(list))