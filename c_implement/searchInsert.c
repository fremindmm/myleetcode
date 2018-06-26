#include<stdio.h>
int searchInsert(int * nums, int numsSize, int target){
    if(numsSize == 0 || nums[0] >=target)
        return 0;
    int i = 0;
    while(i < numsSize - 1){
        if (nums[i] == target) 
            return i;
        else if(nums[i] < target && nums[i+1] >target)
            return i+1;
        else 
            ++i;
    }
    if(nums[numsSize-1] == target) 
        return numsSize - 1;
    else
        return numsSize;
    }

int searchInsert(int* nums, int numsSize, int target) {
    int high = numsSize - 1 , low = 0 , mid = (high + low)/2;
    while(low <= high)
    {
        mid = (high + low)/2;
        if(nums[mid] == target){
            return mid;
        }
        else if(nums[mid] > target){
            high = mid - 1;
        }
        else {
            low = mid + 1;
        }
        
    }
    
    return low;
}
int main(){
    int nums[5]={1,3,4,6};
    int numsSize=4;
    int target = 5;
    int ret =  searchInsert(nums, numsSize, target);
    printf("%d\n", ret);
}
