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

int add(int a ,int b){
    return a + b;
}
int main(){
    base b;
    b.a = 1;
    b.add(2,3);
    return 0;
}