'''
Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap years into a list and display the list.
Also write the pytest test cases to test the program.
'''


#PF-Assgn-22
def find_leap_years(given_year):

    # Write your logic here
    y = list(str(given_year))
    y = y[2:]
    y = ''.join(y)
    list_of_leap_years = []
    nextleap = given_year + 1
    while len(list_of_leap_years)!=15:
        if y=='00':
            if nextleap%400==0:
                list_of_leap_years.append(nextleap)
        elif y!='00':
            if nextleap%4==0:
                list_of_leap_years.append(nextleap)
        nextleap = nextleap + 1
        y = list(str(nextleap))
        y = y[2:]
        y = ''.join(y)
    return list_of_leap_years

list_of_leap_years=find_leap_years(2002)
print(list_of_leap_years)