#include<stdio.h>
#include<string.h>
int strcmp1(char * s, char * t){
    for(;*s++==*t++;)
        //if(*s == '\0')
        if(!*s)
            return 0;
    return(*s-*t);
}
void main()
{
   if ("abcd" == "abcd")
   printf("ok");
   int ret = strcmp1("abc","abc"); 
   if (strcmp1("abcd","ab cd"));
   printf("%d",ret);
   

}
