#include <iostream>
using namespace std;

class Widget {
	public:
	   Widget();
           Widget(const Widget& rhs);
	   Widget& operator=(const Widget& rhs);

};


int main()
{
	Widget w1;
	Widget w2(w1);
}

