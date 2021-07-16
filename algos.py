##Create a function sum() that returns the sum of the two numbers passed as it's arguments: Ex sum(2,5) should return 7

def sum(num1, num2):
    return num1+num2

##Log positive numbers starting at 2019, counting down by 8

def CountDownBy8():
	for i in range(2019, 0, -8):
		print(i)


##Kelvin wants to convert between temperature scales. Create celcius to Fahrenheit(cDegrees) that accepts a number of degrees in Celcius, and returns the equivalent temperature as expressed in Fahrenheit degrees. For review, Fahrenheit = (9/5 * Celcius) + 32

def celciusToFahrenheit(cDegrees):
	return (9/5 * cDegrees + 32)

##Given an array, write a function that changes all positive numbers in the array to "big"

def makeItBig(arr):
	for i in range(0, len(arr)):
		if arr[i] > 0:
			print(arr[i])
			arr[i] = "big"
	return arr


##Write a loop that makes seven calls to console.log to output the following triangle:

#
##
###
####
#####
######
#######


num = '#'
for i in range(1, 8, 1):
    print(num)
    num = num + '#'

