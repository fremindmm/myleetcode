#include<stdio.h>
f(char *s){
   char *p=s;
   while(*p)
       p++;
   return(p-s);
}

main()
{
    char *a="abded";
    int k;
    k=f(a);
    printf("%d", k);
}

