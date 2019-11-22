// Misuse of the preprocessor

/* The #define directive is used to implement macros that looks like functions -- which is wrong
 */

// call f with maximum of a and b
#define CALL_WITH_MAX(a,b) f((a)>(b)?(a):(b))  // Remember to parametrize all arguments in the macro

int main()
{
	int a = 5;
	int b = 0;

	CALL_WITH_MAX(++a, b);
	CALL_WITH_MAX(++a, b+10);
}

// The above is actually nonsense - when actually start using templates


template<typename T>
inline void callWithMax(const T&a, const T&b)
{
	f(a>b ? a:b)
}

/* This is introduction into templates
 * This generates a whole family of functions - each takes 2 objects of the same type
 * CallWithMax() - is a real function
 */

/* THINGS TO REMEMBER
 *
 * For simple constants - prefer const objects or enums to #defines
 * For function like macros, prefer inline function to #defines.
