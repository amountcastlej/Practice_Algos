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

#String Times
#Given a string & a non-negative int n, return a larger string that is is n copies of the original string
def string_times(str, n):
	return str * n
	result = ""
	for i in range(n):
		result += str
	return result
string_times('Hi', 2)
string_times('Hi', 3)
string_times('Hi', 1)

#Front Times
#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front
def front_times(str, n):return str[:3] * n
	front_len = 3
	for i in range(n):
		result = result + front
	return result
front_times('Chocolate', 2)
front_times('Chocolate', 3)
front_times('Abc', 3)

#String Bits
#Given a string, return a new string made of every other char starting with the first, so "hello" yields "hlo"
def string_bits(str):return str[::2] => [start:stop:step]
	result = ""
	for i in range(len(str)):
		if i % 2 == 0:result = result + str[i]
	return result
string_bits('Hello')
string_bits('Hi')
string_bits('Heeololeo')

#Missing CharGiven a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string
def missing_char(str, n):
	front = str[:n]
	back = str[n+1:]  
	return front + back
missing_char('kitten', 1)
missing_char('kitten', 0)
missing_char('kitten', 4)

#String Times
#Given a string & a non-negative int n, return a larger string that is is n copies of the original string
def string_times(str, n):
	return str * n
	result = ""
	for i in range(n):
		result += str
	return result
string_times('Hi', 2)
string_times('Hi', 3)
string_times('Hi', 1)

#Front BackGiven a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
	if len(str) <= 1:
		return str
	mid = str[1:len(str)-1]
	return str[len(str)-1] + mid + str[0]
front_back('code')

#array_count9
#Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
	nines = 0
	for i in range(len(nums)):
		if nums[i] == 9:
			nines += 1
	return nines
array_count9([1, 2, 9])
array_count9([1, 9, 9])
array_count9([1, 9, 9, 3, 9])

#Array front9
#Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4

def array_front9(nums):
	end = len(nums)
	if end > 4:
		end = 4
	for i in range(end):
		if nums[i] == 9:
    			return True
	return False
array_front9([1, 2, 9, 3, 4])
array_front9([1, 2, 3, 4, 9])
array_front9([1, 2, 3, 4, 5])

#Array123
#Given an array of ints, return True if the sequence of numbers 1,2,3 appears in the array somewhere
def array123(nums):
	for i in range(len(nums)-2):
    	if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
		return True
	return False
array123([1, 1, 2, 3, 1]) 
array123([1, 1, 2, 4, 1])
array123([1, 1, 2, 1, 2, 3])