'''
Write a function, check_palindrome() to check whether the given string is a palindrome or not. The function should return true if it is a palindrome else it should return false.

Note: Initialize the string with various values and test your program. Assume that all the letters in the given string are all of the same case. Example: MAN, civic, WOW etc. 

Also write the pytest test cases to test the program.
'''
#PF-Assgn-31
def check_palindrome(word):
    k = list(word)
    l = k[::-1]
    for i in range(0,len(k)):
        a = k[i]
        b = l[i]
        if a==b:
            pass
        else:
            return False
    return True
    #Remove pass and write your logic here

status=check_palindrome("abcdcba")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")