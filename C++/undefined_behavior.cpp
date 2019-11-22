#include <iostream>
using namespace std;

/*
 * This is a classic case of undefined behavior
 * Seg Faults are created when one tries to access memory, that one doesn't belong to.
 */


int main()
{
	int *p = 0;  // deferencing a null pointer - results in a segmentation fault
	cout<<*p; 
}
