#include <iostream> //include header library for input % output

using namespace std; //include standard library

int main() // define main function
{
	int x1 = 0, x2 = 1, x3, y, answer; // create int variables for use in program.
	//Output text to prompt user for amount of elements in Fibonacci sequence.
	cout << "Enter the number of elements in Fibonacci sequence: ";
	//Get User input
	cin >> answer;
	//Output sequence elements
	cout << "The Fibonacci sequence is : " << x1 << " " << x2 << " ";
	//Create for loop to build Fibonacci sequence program logic
	for (y = 2; y < answer; ++y) //If y is less than amount in sequence continue logic.
	{
		x3 = x1 + x2; // x3 variable equals x1 + x2
		cout << x3 << " "; //output x3 variable and a space between each iteration.
		x1 = x2; // set x1 variable equal to x2
		x2 = x3; // set x2 variable equal to x3
	}
	return 0; // End program
}

