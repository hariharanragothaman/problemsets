/* Some of the useful applications of const is in function declarations
 *
 * Within a function declaration, 'const' can refer to the 
 *           1. function's return value
 *           2. to individual parameters
 *           3. for memeber functions, to the function as a whole..
 */

class Rational {...};

const Rational operator*(const Rational& lhs, const Rational& rhs);

// Why is the result of operator* be a const object?
// Eg: Rational a,b,c;
//     (a*b) = c;
//
//
//     OHHHH!!! So, if we want the clients not to operate on the data that it returns
//     then making it into "const" makes sense..


/* const Member functions  */

/* 1. They make the class easier to understand
 * 2. 
