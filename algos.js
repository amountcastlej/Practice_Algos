//Create a function sum() that returns the sum of the two numbers passed as it's arguments: Ex sum(2,5) should return 7

function sum(num1, num2){
    return num1+num2
}

//Log positive numbers starting at 2019, counting down by 8

function CountDownBy8(){
	for (var i = 2019; i > 0; i-=8){
		console.log(i);
	}


//Kelvin wants to convert between temperature scales. Create celcius to Fahrenheit(cDegrees) that accepts a number of degrees in Celcius, and returns the equivalent temperature as expressed in Fahrenheit degrees. For review, Fahrenheit = (9/5 * Celcius) + 32

function celciusToFahrenheit(cDegrees){
	f = (9/5 * cDegrees) + 32
	return f

//Given an array, write a function that changes all positive numbers in the array to "big"

function makeItBig(arr){
	for (var i = 0; i < arr.length; i++){
		if (arr[i] > 0){
			console.log(arr[i], ' is positive!');
			arr[i] = "big";
		}
	}
	return arr;


//Write a loop that makes seven calls to console.log to output the following triangle:

// #
// ##
// ###
// ####
// #####
// ######
// #######

// let num = '#';
// for (let i = 1; i <=7; i += 1) {
//     console.log(num);
//     num = num + '#';
// }
