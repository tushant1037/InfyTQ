'''
A 10-substring of a number is a substring of its digits that sum up to 10.

For example, the 10-substrings of the number 3523014 are:
3523014, 3523014, 3523014, 3523014

Write a python function, find_ten_substring(num_str) which accepts a string and returns the list of 10-substrings of that string.

Handle the possible errors in the code written inside the function.

Sample Input	Expected Output
'3523014'	   ['5230', '23014', '523', '352']
'''
#PF-Assgn-41
def find_ten_substring(num_str):
    num_str = list(num_str)
    n = len(num_str)
    subarr = []
    for i in range(1,n):
        for j in range(0,n+1-i):
            sub = num_str[j:j+i]
            s = 0
            for k in sub:
                s = s + int(k)
            if s==10:
                subarr.append(sub)
    out = []
    for i in subarr:
        j = "".join(i)
        out.append(j)
    return out
        
    #Remove pass and write your logic here

num_str="3523014"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)