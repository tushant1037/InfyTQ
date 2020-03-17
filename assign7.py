'''
Write a python program to generate and display the next date of a given date.

Assume that
Date is provided as day, month and year as shown in below table.
The input provided is always valid. Output should be day-month-year.
Hint: print(day,"-",month,"-",year) will display day-month-year

Sample Input	Expected Output
Day	    1	    2-9-2015
Month	9
Year	2015

Also identify the test data and use it to test the program.'''

#PF-Tryout

def generate_next_date(day,month,year):
    y = list(str(year))
    y = y[2:]
    y = ''.join(y)
    month_days_31 = [1,3,5,7,8,10,12]
    month_days_30 = [4,6,9,11]
    month_days_29_28 = [2]
    if y=='00':
        if year%400==0:
            if month in month_days_31:
                if day!=31:
                    next_day = day + 1
                    next_month = month
                    next_year = year
                elif day==31:
                    if month!=12:
                        next_day = 1
                        next_month = month+1
                        next_year = year
                    elif month==12:
                        next_day  = 1
                        next_month = 1
                        next_year = year+1
                        
            elif month in month_days_30:
                if day!=30:
                    next_day = day + 1
                    next_month = month
                    next_year = year
                elif day==30:
                    if month!=12:
                        next_day = 1
                        next_month = month+1
                        next_year = year
                    elif month==12:
                        next_day  = 1
                        next_month = 1
                        next_year = year+1
                        
            elif month in month_days_29_28:
                if day!=29:
                    next_day = day + 1
                    next_month = month
                    next_year = year
                elif day==29:
                    if month!=12:
                        next_day = 1
                        next_month = month+1
                        next_year = year
                    elif month==12:
                        next_day  = 1
                        next_month = 1
                        next_year = year+1
        else:
            if month in month_days_31:
                if day!=31:
                    next_day = day + 1
                    next_month = month
                    next_year = year
                elif day==31:
                    if month!=12:
                        next_day = 1
                        next_month = month+1
                        next_year = year
                    elif month==12:
                        next_day  = 1
                        next_month = 1
                        next_year = year+1
            elif month in month_days_30:
                if day!=30:
                    next_day = day + 1
                    next_month = month
                    next_year = year
                elif day==30:
                    if month!=12:
                        next_day = 1
                        next_month = month+1
                        next_year = year
                    elif month==12:
                        next_day  = 1
                        next_month = 1
                        next_year = year+1
            elif month in month_days_29_28:
                if day!=28:
                    next_day = day + 1
                    next_month = month
                    next_year = year
                elif day==28:
                    if month!=12:
                        next_day = 1
                        next_month = month+1
                        next_year = year
                    elif month==12:
                        next_day  = 1
                        next_month = 1
                        next_year = year+1
    else:
        if year%4==0:
            if month in month_days_31:
                if day!=31:
                    next_day = day + 1
                    next_month = month
                    next_year = year
                elif day==31:
                    if month!=12:
                        next_day = 1
                        next_month = month+1
                        next_year = year
                    elif month==12:
                        next_day  = 1
                        next_month = 1
                        next_year = year+1
            elif month in month_days_30:
                if day!=30:
                    next_day = day + 1
                    next_month = month
                    next_year = year
                elif day==30:
                    if month!=12:
                        next_day = 1
                        next_month = month+1
                        next_year = year
                    elif month==12:
                        next_day  = 1
                        next_month = 1
                        next_year = year+1
            elif month in month_days_29_28:
                if day!=29:
                    next_day = day + 1
                    next_month = month
                    next_year = year
                elif day==29:
                    if month!=12:
                        next_day = 1
                        next_month = month+1
                        next_year = year
                    elif month==12:
                        next_day  = 1
                        next_month = 1
                        next_year = year+1
        else:
            if month in month_days_31:
                if day!=31:
                    next_day = day + 1
                    next_month = month
                    next_year = year
                elif day==31:
                    if month!=12:
                        next_day = 1
                        next_month = month+1
                        next_year = year
                    elif month==12:
                        next_day  = 1
                        next_month = 1
                        next_year = year+1
            elif month in month_days_30:
                if day!=30:
                    next_day = day + 1
                    next_month = month
                    next_year = year
                elif day==30:
                    if month!=12:
                        next_day = 1
                        next_month = month+1
                        next_year = year
                    elif month==12:
                        next_day  = 1
                        next_month = 1
                        next_year = year+1
            elif month in month_days_29_28:
                if day!=28:
                    next_day = day + 1
                    next_month = month
                    next_year = year
                elif day==28:
                    if month!=12:
                        next_day = 1
                        next_month = month+1
                        next_year = year
                    elif month==12:
                        next_day  = 1
                        next_month = 1
                        next_year = year+1
    #Start writing your code here

    print(next_day,"-",next_month,"-",next_year)


generate_next_date(22,3,2011)