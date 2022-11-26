#include <iostream>
using namespace std;

#define DEBUG true

int main() {
    char c = 'c';
    bool b = true;
    int i = 1;
    char* s = "string";
    float f = 3.14;
    double d = 1.61;

    i *= b || i && c;

    for (; i < 10; i++) {
        if (DEBUG) {
            cout << c << b << i << s << (f + d / i);
        }
    }

}