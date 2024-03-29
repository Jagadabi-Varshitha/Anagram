#def check(s1,s2):
#    if(sorted(s1)==sorted(s2)):
#        print("True")
#   else:
#       print("False")
#s1="listen"
#s2="silent"
#check(s1,s2)
def are_anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    if len(str1) != len(str2):
        return False
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False  
    for count in char_count.values():
        if count != 0:
            return False

    return True
str1 = input().strip()
str2 = input().strip()
print(are_anagrams(str1, str2))



    