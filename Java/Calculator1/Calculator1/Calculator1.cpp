#include <iostream>
#include "Calculator.h"

using namespace std;

int main()
{
	double x = 0.0;
	double y = 0.0;
	double final = 0.0;
	char op = '+';

	cout << "C++ Basic Calculator" << endl << endl;
	cout << "Please Enter your equation. Format: a+b | a-b | a*b | a/b"
		<< endl;

	Calculator c;
	while (true)
	{
		cin >> x >> op >> y;
		if (op == '/' && y == 0)
		{
			cout << "Division by 0 is not allowed." << endl;
			continue;
		}
		final = c.Calculate(x, op, y);
		cout << "The solution is, " << final << endl;

	}
	return 0;
}