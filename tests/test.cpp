#include <iostream>
#include <iomanip>
#include <limits>
#include <typeinfo>
using namespace std;
#define DEBUG true

class MyClass {

    MyClass() {
        std::cout << "MyClass constructor" << std::endl;
    }

    int some_function(int a) {
        return a;
    }

};

int main() {
    char c = 'c';
    c = 'd';
    bool b = true;
    int i = 1;
    char* s = "string";
    float f = 3.14;
    double d = 1.61,d1=58.,d2=4e2,d3=123.456e-7;
    /* 
        multiline comment
    */
    i *= b || i && c;
    std::cout
        << OUT( 123.456e-67f   ) // float, truncated to zero
        << OUT( .1E4f          ) // float
        << OUT( 0x10.1p0       ) // double
        << OUT( 0x1p5          ) // double
        << OUT( 0x1e5          ) // integer literal, not floating-point
        << OUT( 3.14'15'92     ) // double, single quotes ignored (C++14)
        << OUT( 1.18e-4932l    ) // long double
        << OUT( 3.4028234e38f  ) // float
        << OUT( 3.4028234e38   ) // double
        << OUT( 3.4028234e38l  ) // long double
        << '\n';
    for (; i < 10; i++) {
        if (DEBUG) {
            cout << c << b << i << s << (f + d / i);
        }
    }

}