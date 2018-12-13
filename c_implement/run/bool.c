#include<stdio.h>

void main(){
    int a, b, c;
    a=1;b=2;c=3;
    a=b--<=a||a+b!=c;
    printf("%d,%d", a,b);
}
