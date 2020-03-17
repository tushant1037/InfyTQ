'''
Write a python function, check_double(number) which accepts a whole number and returns True if it satisfies the given conditions.

The number and its double should have exactly the same number of digits.
Both the numbers should have the same digits ,but in different order.
Otherwise it should return False.

Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but in a different order.


'''
#PF-Assgn-38

def check_double(number):
    num1 = str(number)
    num1 = list(num1)
    print(num1)
    num2 = number*2
    num2 = str(num2)
    num2 = list(num2)
    print(num2)
    if len(num1)==len(num2):
        for i in num1:
            if i in num2:
                num2.remove(i)
            else:
                return False
        if len(num2)==0:
            return True
        else:
            return False
    else:
        return False
    #Remove pass and write your logic here

#Provide different values for number and test your program
print(check_double(245))