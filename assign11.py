'''
The program provided in the starter code tab is written to display “*” as per the expected output given below. But the code is having logical errors, debug the program using Eclipse Debugger and correct it.

Estimated Time: 15 minutes

Expected Output:
*****
****
***
**
*

counter1=0
counter2=5
while(counter1 < 5):
  star=""
  while(counter2>counter1):
     star=star+ "*"
     counter2-=1
  print(star)
  counter1+=1
'''
counter1=0
counter2=5
while(counter1 < 5):
  star=""
  while(counter2>counter1):
     star=star+ "*"
     counter2-=1
  print(star)
  counter1+=1
  counter2 = 5