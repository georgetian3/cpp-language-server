#include<iostream>
class base{
    public:
        int a;
        int b;
        int add(int a,int b){
            return a+b;
        }
    private :
        int c;
    
};

// test


class base1{};
int add(int a ,int b){
    int flag = 0;
    return a + b;
}
int main(){
    base b;
    b.a = 1;
    b.a = 1;
    b.add(2,3);
    return 0;
}