#include <iostream>
#include <iomanip>
#include <limits>
#include <typeinfo>
#include "myheader.h"

class MyClass {

    MyClass() {
        cout << "MyClass constructor" << endl;
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