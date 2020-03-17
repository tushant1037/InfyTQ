'''
Write a python program which finds the maximum number from num1 to num2 (num2 inclusive) based on the following rules.

1. Always num1 should be less than num2
2. Consider each number from num1 to num2 (num2 inclusive). Populate the number into a list, if the below conditions are satisfied
    a. Sum of the digits of the number is a multiple of 3
    b. Number has only two digits
    c. Number is a multiple of 5
3. Display the maximum element from the list
In case of any invalid data or if the list is empty, display -1.

'''
#PF-Assgn-28

def find_max(num1, num2):
    max_num=-1
    if num2<=num1:
        return max_num
    arr = []
    for i in range(num1,(num2)+1):
        if i%3==0 and i%5==0:
            arr.append(i)
    out = []

    for i in arr:
        k = list(str(i))
        if len(k)==2:
            l = ''.join(k)
            out.append(l)
    if len(out)!=0:
        g = out[-1]
    else:
        return -1
    return int(g)
            
    # Write your logic here

#Provide different values for num1 and num2 and test your program.
max_num=find_max(2,14)
print(max_num)