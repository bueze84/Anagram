# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


# def find_anagram(word, anagram):
#     # [assignment] Add your code here
#     word = word.lower()
#     anagram = anagram.lower()
#     if len(word) != len(anagram):
#         return False
    
#     for c in word:
#         if c not in "silent":
#             break
#     return True

def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = [w for w in sorted(word.lower()) if not w.isspace()]
    anagram = [w for w in sorted(anagram.lower()) if not w.isspace()]
    
    print(word, anagram)
    if len(word) != len(anagram):
        return False
    
    if word != anagram:
        return False
    
    return True

def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = sorted(word.lower()) 
    anagram = sorted(anagram.lower())
    
    print(word, anagram)
    if len(word) != len(anagram):
        return False
    
    if word != anagram:
        return False
    
    return True


print(find_anagram("silent", "siletn"))
print(find_anagram("coronavirus", "carnivorous"))
print(find_anagram("restful", "fluster"))
print(find_anagram("forty five", "over fifty"))
print(find_anagram("funeral" ,"real fun"))


# for c in "listen":
#     if c not in "silent":
#         break
# else:
#     print("Good")