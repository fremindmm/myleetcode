#include<stdio.h>
#define N 5
#define M N+1
#define f(x) (x*M)
void main(){
    int i,j;
    i=f(2);
    j=f(1+1);
    printf("%d %d\n", i,j);
}

