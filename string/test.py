#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 2019/2/10 下午12:52
# @Author         : Jeckxie
# @CopyRight      : 2018-2020 OpenBridge by yihecloud
# @File           : test.py
# @Product        : PyCharm
# @Docs           : 
# @Source         :
class Solution(object):

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        def check_include(s1, s2):
            alist1 = []
            for i in range(26):
                alist1.append(0)
            alist2 = alist1[:]
            for i in s1:
                alist1[ord(i) - 97] += 1
            for i in s2:
                alist2[ord(i) - 97] += 1
            if alist1 == alist2:
                return True
            else:
                return False

        def is_in(first):
            if len(s1) == len(s2) and len(s1) == 1 and s1 != s2:
                return False
            if first in s2:
                start = s2.index(first)
                end = start + len(s1)
            else:
                return False
            left_len = len(s2) - start - len(s1)
            if left_len < 0:
                return False
            s2_sub1 = s2[start:end]
            return check_include(s1, s2_sub1)

        for i in s1:
            if is_in(i):
                return True
        else:
            return False



    bool checkInclusion(string s1, string s2) {
        int len1=s1.length(),len2=s2.length();
        if(len1>len2) return false;
        vector<int> S(26);
        vector<int> V(26);
        for(int i=0;i<len1;i++){
            S[s1[i]-97]++;
            V[s2[i]-97]++;
        }
        for(int i=0;i<len2-len1+1;i++){
            if(S==V) return true;
            if(i<len2-len1){
                V[s2[i]-97]--;
                V[s2[i+len1]-97]++;
            }
        }
        return false;
    }




     def checkInclusion(s1,s2):
         len1 = len(s1)
         len2 = len(s2)
         if len1 > len2:
             return False
         sl1 = [0 for i in range(26)]
         sl2 = sl1[:]

         for i in xrange()



if __name__ == "__main__":
    s = Solution()
    #print s.checkInclusion('ab','eidbaooo')
    print s.checkInclusion('adc','dcda')
