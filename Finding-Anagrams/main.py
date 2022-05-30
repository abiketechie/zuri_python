# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
   
    str1 = word.lower()
    str2 = anagram.lower()

    if len(str1) == len(str2):
        
        sort_str1 = sorted(str1)
        sort_str2 = sorted(str2)

        if sort_str1 == sort_str2:
            print("True")
        
        else:
            print("False")
    else:
        print("The word is not of the same length")
    return True

find_anagram("beleow", "erlbow") # False
find_anagram("scar", "cars") # True






   




   

