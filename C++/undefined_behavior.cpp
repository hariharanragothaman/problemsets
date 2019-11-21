#include <iostream>
using namespace std;

/*
 * This is a classic case of undefined behavior
 */


int main()
{
	int *p = 0;  // deferencing a null pointer - results in a segmentation fault
	cout<<*p; 
}
