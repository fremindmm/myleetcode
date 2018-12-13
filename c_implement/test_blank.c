#include<stdio.h>
#define N 5
#define M N+1
#define f(x) (x*M)
/*
f(char *s){
    char *p = s;
    while(*p)
        p++;
    return(p-s);
}*/

int main(){

/*    int a, b, c;
    a=1;b=2;c=3;
    a=b--<=a||a+b!=c;
    printf("%d,%d",a,b);
*/
/*    char *a = "abded";
    int k;
    k=f(a);
    printf("%d", k);
*/
/*
    int i,j;
    i = f(2);
    j = f(1+1);
    printf("%d %d\n", i,j);
*/
    FILE *fp;
    int d1,d2,a[6]={1,2,3,4,5,6};
    fp = fopen("file.data", "w");
    fprintf(fp, "%d%d%d\n",a[0],a[1],a[2]);
    fprintf(fp, "%d%d%d\n",a[3],a[4],a[5]);
    fclose(fp);
    fp=fopen("file.dat", "r");
    fscanf(fp, "%d%d",&d1,&d2);
    printf("%d %d\n",d1,d2);
    fclose(fp);
}
