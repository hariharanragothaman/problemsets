#include <iostream>
using namespace std;

class Foo
{
	private:
	int m_foo;

	public:
	// single parameter constructor, that can be used for implicit conversions
        explicit Foo (int foo) : m_foo(foo)
	{
		
	}

	int GetFoo()
	{
		return m_foo;
	}

};


void DoBar ( Foo foo)
{
	int i = foo.GetFoo();
}

int main()
{
	DoBar(Foo(42));
	// If you remove the explicit keyword - you can just do - DoBar(42)
}
