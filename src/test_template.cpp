
#include <iostream>
using X = int;
struct A {};
template<const X& x, int i, A a> void f() {
i++; // error: change of template-parameter value
&x; // OK
&i; // error: address of non-reference template-parameter
&a; // OK
int& ri = i; // error: non-const reference bound to temporary
const int& cri = i; // OK: const reference bound to temporary
const A& ra = a; // OK: const reference bound to a template parameter object
}