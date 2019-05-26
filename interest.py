#calculates simple interest
#formula>>>> simpleinterest = principal*rate*time

#we are going to let the rate be constant
rate = 0.12

#the principal is going to be input by the banker
principal = int(input("Enter the principal amount"))

#the time is going to be input by the banker coz it changes
time = int(input("Enter the time in years"))

#we now calculate the simple interest
interest = principal*rate*time

#we now output the simple interest and use string formatting to insert it into a string
print("The simple interest is: {}".format(interest))