#define ASPECT_RATIO 1.653


/*
 * #define is not even treated as part of the language
 * Won't even be seen by the compilers
 * So the name aspect ratio may not get into the symbol table.
 * Note: Upper case is prefered for macros
 *
 * While running or compiling, when we may get a refence to 1.653 and not APSECT_RATIO
 * Also this might result in multiple copies in the object code
 *
 * Solution to this is the following
 *
 *
 */

const double AspectRatio = 1.653

/*
 * Now this will definitely be seen by compilers and will enter into the symbol table
 * Also this does not result in multiple copies in object code
 */


/* Special Scenarios, while replacing #defines with constants
 *  When replacing #defines with constants 2 special cases are worth mentioning.
 *
 *  1. Defining constant pointers
 *  2. Class specific constants
 *
 *  Note: constants are generally put in header files.
 *  
 *  Scenario #1:
 *
 *  It's important for the pointer to be constant
 *  Defining a constant char*-based string
 *
 */

const char* const authorName = "Scott Meyers"  // To read more on this refer Item3 section

// string objects are generally preferable to their char*-based progenitors. So....
//

const std:string authorName("Scott Meyers")

/* Scneario #2: "Class specific constants"
 */

class GamePlayer {
	private:
		static const int NumTurns = 5;  // btw, it's kinda illegal to assign value to a static member!!!
		int scores[NumTurns];
	};

// int scores[NumTurns] -- is a declaration and not a definition???? Why is that?
// That's correct. Definition is assigning it to a value.. Putting a label on it.
//
// Note: C++ requires you to provide a declaration for anything you use.


const int GamePlayer::NumTurns;  // This is a definition  and is in the implementation file, and not in a header file

// intialization and declaration happen together. And remember #define don't respect scope.
// So changing it as this.


class CostEstimate{
	private:
		static const double FudgeFactor; // declaration of static class constant -- goes in the header file
		//...
	};

const double CostEstimate::FudgeFactor = 1.35; // Definition goes in implementation file

// What's the enum hack?

class GamePlayer 
{
	private:
		enum {NumTurns = 5};
		int scores[NumTruns];
		//...
};

/* 
 * This enum hack is important if one does not want, users of the class to get an address of the pointer to your integral constants
 * The enum hack is a fundamental technique in template metaprogramming.
 */

