#include <iostream>
using namespace std;

#define DEBUG true

int main() {
    char c = 'c';
    c = 'd';
    bool b = true;
    int i = 1;
    char* s = "string";
    float f = 3.14;
    double d = 1.61;
    /* 
        multiline comment
    */
    i *= b || i && c;
    // single line comment
    for (; i < 10; i++) {
        if (DEBUG) {
            cout << c << b << i << s << (f + d / i);
        }
    }

}