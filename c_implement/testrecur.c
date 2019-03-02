#include<stdio.h>
void recur(int num){
  if (num == 0) return;
  else printf("%d", num);
  recur(num--);
}
int main(void){
  recur(3);

}

