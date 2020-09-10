/* Use const whenever possible */

/* The wonderful thing about 'const', is that it allows you to specify a semantic constraint
 * ------ a particular object should not be modified ----------
 *
 *  It tells the compiler that the value should remain invariant
 */

char greeting[] = "Hello";

char *p = greeting  		// non-const pointer & non-const data

const char *p = greeting 	// non-const pointer & const data
 
char* const p = greeting;       // const pointer & non-const data

const char* const p 		// const pointer * const data

// Why is this syntax like this? What's the trick? (or) formulae

// If the word const appears to the left of the asterisk, what's pointed to is constant
// If the word const appears to the right of the asterisk, the pointer itself is constant
// If the const appears on both sides, both are constant

// -------------------------------------------------------------------------------------


void f1(const Widget *pw); // here f1 is a function that takes a pointer to a const Widget object
		           // since it's to the left, what's pointer to is constant

// The thing to learn here is... the above line can also be written as

void f1( Widget const *pw); // Honestly this makes more sense to me, anyway

// The STL analogue of const T* pointer is based on the above concept 
