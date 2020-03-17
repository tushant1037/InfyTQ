'''
Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.

Write a python function which performs the run length encoding for a given String and returns the run length encoded String.

Provide different String values and test your program.

Sample Input	Expected Output
AAAABBBBCCCCCCCC	4A4B8C
AABCCA	            2A1B2C1A
'''

#PF-Assgn-30
def encode(message):
    k = list(message)
    if len(k)==1:
        return "1"+message
    arr = []
    l = []
    for i in range(0,len(k)):
        a = k[i]
        for j in range(i,len(k)):
            b = k[j]
            if a!=b:
                ind = j
                break
        l.append(a)
        arr.append(ind)
    arr = set(arr)
    arr = list(arr)
    #print(arr)
    arr2 = [0]
    for i in arr:
        arr2.append(i)
    arr2.append(len(k))
    
    outstr=""
    #print(len(k))
    for j in range(0,len(arr2)):
        a = arr2[j]
        n = k[a]
        #print(a)
        #print(n)
        
        b = arr2[j+1]
        
        #print(b)
        sub = k[a:b]
        le = len(sub)
        outstr = outstr + str(le) + n
        if b==len(k):
            break
    return outstr
        
            
            
    
                
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)