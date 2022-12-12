#include <iostream>
#include <iomanip>
#include <limits>
#include <typeinfo>
#include "myheader.h"

class MyClass {

    MyClass() {
        cout << "MyClass constructor\n";
    }

    int member_function(int a = 1) {
        return a;
    }

    ~MyClass() {
        cout << "MyClass destructor\n";
    }

};

int another_function(char* str) {
    return str[0];
}

int main() {
    char c = 'c';
    c = 'd';
    bool b = true;
    char* s = "string";
    float f = -3.14;
    MyClass instance;
    int test = instance.member_function(2);
    test = instance.member_function();
    test = another_function(s);

    int a = a || a && a;
    a = a + a - a * a / a;
    a = a | a & a ^ a;
    a = a << (a >> a);
    a += 1;
    a -= 1;
    a *= 1;
    a /= 1;
    a <<= 1;
    a >>= 1;

    while (test--) {
        cout << "while loop\n";
    }
 
    for (int i = 0; i < 10; i++) {
        cout << "for loop\n";
    }

    if (c == 'd') {
        cout << "if conditional\n";
    }

}