#include <iostream>
#include <iomanip>
#include <limits>
#include <typeinfo>
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
 
    for (; i < 10; i++) {
        if (DEBUG) {
            cout << c << b << i << s << (f + d / i);
        }
    }

}