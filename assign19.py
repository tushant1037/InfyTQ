'''
Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.

Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.



Sample Input	                   Expected output
"I like Python"
"Java is a very popular language"	  lieyon
'''
#PF-Assgn-33

def find_common_characters(msg1,msg2):
    msg1 = list(msg1)
    
    msg2 = list(msg2)
    
   
    out = []
    for i in msg1:
        for j in msg2:
            if i==j:
                out.append(i)
    st = ""
    for i in out:
        if i==" ":
            pass
        elif i not in st:
            st = st + i
    if len(st)==0:
        return -1
    else:
        return st
            

#Remove pass and write your logic here

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)