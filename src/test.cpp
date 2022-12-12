#include <iostream>
#include <iomanip>
#include <limits>
#include <typeinfo>

class student{
    int id;
    char stu;
    void eat(){
        return;
    }
};

int main() {
    char c = 'c';
    c = 'd' ;
    int a = 1;
    int b = 1;
    if (a == b){
        a = 3;
        b = 4;
    }

    student kennyl;

    return 0;
}