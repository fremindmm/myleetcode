#include<stdio.h>
#include<stdlib.h>
int main(void)
{
    int val, temp, n, sum = 0;
    int i;
    printf("please input data and number of executions\n");
    scanf("%d %d", &val, &n);
    temp = val;
    if(val <=0 || val>=10)
    {
        printf("ERROR");
    }
    else
    {
        for(i=1;i<=n; i++)
        {
            sum = sum + val;
            val = val*10 + temp;
        }
        printf("%d", sum);
    }
    printf("\n");
    return 0;
}
