#include <iostream>

// test program
class Student{
public:
    int a = 1;
    long b = 2L;
    char s = 's';
    char t = u8't';
    char* str = "asjdfoa";
    double lit = 0.0;
    bool educated = true;
    int add(int c, int d){
        int in_class_function = 0;
        return c+d;
    }
    bool checkOdd(int num){
        if (num % 2 == 0){
            return false;
        }
    }
};

int subtract(int a, int b){
    int in_function; //testing for domain
    return a-b;
}

/* this is
 another type
 of comment
*/

int main(){
    int in_main = 2;
    Student alpha;
    alpha.lit = 3.2;
    int fa = 1;
    alpha.add(in_main,fa);
    if((in_main < fa) || (in_main >= 0)){
        in_main = in_main - fa;
    }
    alpha.educated = alpha.checkOdd(in_main);
    int count = 0;
    for(int a=0; a<3; a++){
        count++;
    }
    return 0;
}