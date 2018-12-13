#include<stdio.h>

int fun(int n)
{
    int count = 0;
    while(n){
        count++;
        n=n/10;
    }
    return count;
}

void main(){
   int ret= fun(1111);
   printf("%d\n",ret);
}
