#include <iostream>
#define moo 37

using namespace std;
int main(int argc, char *argv[]) {
	const int age = 68;
	const string newline = "\n";
	int data = 56;
	data = 46;
	
	// The "newline" constant in play: //
	cout << "Cows go MOOOOOOO: " << moo << newline;
	
	// A simple program showing basic integers: //
	cout << "Age: " << age << "\nData: " << data << "\n";
	
	// Yet the same thing, but with actual mathematical stuff: //
	cout << "Age: " << age + 5 << "\nData: " << data - 4 << "\n";
	
	// Basic Maths: //
	cout << "Age: " << age / 5 << "\nData: " << data * 4 << "\n";
	cout << "moo: " << (age / 5) * 5;
	return 0;
}