'''
Write a python function find_duplicates(), which accepts a list of numbers and returns another list containing all the duplicate values in the input list. If there are no duplicate values, it should return an empty list.

Also write the pytest test cases to test the program.

Sample Input	                         Expected Output
[12,54,68,759,24,15,12,68,987,758,25,69]	[12, 68]
'''
#PF-Assgn-44

def find_duplicates(list_of_numbers):
    dup = []
    k = list_of_numbers
    for i in range(0,len(list_of_numbers)):
        a = list_of_numbers[i]
        n = len(list_of_numbers)
        for j in range(i+1,n):
            b = list_of_numbers[j]
            if a==b:
                dup.append(b)
                #k.remove(b)
                #k.remove(a)
    dup = set(dup)
    dup = list(dup)
    return dup
                
            
    #start writing your code here

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)