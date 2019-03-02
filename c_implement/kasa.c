#include<stdio.h>
#include<string.h>
int main()
{
    char* s="GoldenGlobalView";
    char d[20];
    memcpy(d,s,(strlen(s)+1));        //+1 是为了将字符串后面的'\0'字符结尾符放进来，去掉+1可能出现乱码
    printf("%s",d);
    getchar();

    char a[95];
    char aa[95] = "AOL XBPJR IYVDU MVE QBTWZ VCLY AOL SHGF KVN VM JHLZHY HUK FVBY BUPXBL ZVSBAPVU PZ ZSYKULNTZTOS";
    for(int n = 1; n<=25; n++)
    {
        printf("%d\n", n);
        memcpy(a, aa, 95);
        for(int i=0; i<94; i++)
        {
            if(a[i]!=' ')
            {
            //65 A ,65+25=90 Z, 97 a , 97+25 = 122 z
                a[i]=((a[i]-65+n)%26+26)%26+65;
            }
        }
        for(int i=0; i<94; i++)
        {
            printf("%c", a[i]);
        }
        printf("\n");
    }
    return 0;
}



