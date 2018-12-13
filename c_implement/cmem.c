#include<stdio.h>
int a = 0;
char *p1;

main(){
    int b;
    char s[] = "abc";
    char *p2;
    char *p3 = "123456";//"123456" 在常量区，p3 在栈上
    static int c = 0;//全局静态初始化区
    p1 = (char *)malloc(10);
    p2 = (char *)malloc(20);//内存空间在堆区
    strcpy(p1, "123456")
    


}
