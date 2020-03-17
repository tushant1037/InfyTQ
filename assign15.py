'''
The road transport corporation (RTC) of a city wants to know whether a particular bus-route is running on profit or loss.

Assume that the following information are given:
Price per litre of fuel = 70
Mileage of the bus in km/litre of fuel = 10
Price(Rs) per ticket = 80

The bus runs on multiple routes having different distance in kms and number of passengers.
Write a function to calculate and return the profit earned (Rs) in each route. Return -1 in case of loss.

Also write the pytest test cases to test the program.
'''
#PF-Assgn-29
def calculate(distance,no_of_passengers):
    outcome = distance*70/10
    income = no_of_passengers*80
    if outcome>income:
        print(-1)
    else:
        print(income-outcome)
    #Remove pass and write your logic here



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))