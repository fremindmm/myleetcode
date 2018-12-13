#include<stdio.h>

int longestCommonSubstring_n3(const string& str1, const string& str2)
{
   size_t size1 = str1.size();
   size_t size2 = str2.size();
   if(size1 == 0 || size2 == 0)
       return 0;
   int start1 = -1;
   int start2 = -1;
   int longest = 0;
   
   int comparisons = 0;
   
   for (int i = 0; i< size1; ++i)
   {
       for( int j = 0; j< size2; ++j)
       {
           int length = 0;
           int m = i;
           int n = j;
           while(m < size1 && n < size2)
           {
               ++comparisons;
               if(str1[m] != str2[n])
                   break;
               ++length;
               ++m;
               ++n;
           }
           if (longest < length)
           {
               longest = length;
               start1 = i;
               start2 = j;
           }
       }
   }   
}


