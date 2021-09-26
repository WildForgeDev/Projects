#include "Calculator.h"
#include <iostream>

using namespace std;

double Calculator::Calculate(double x, char op, double y)
{
	switch (op)
	{
	case '+':
		return x + y;
	case '-':
		return x - y;
	case '*':
		return x * y;
	case '/':
		return x / y;
	default:
		cout << "You have entered an invalid operator";
		break;
	}
}
