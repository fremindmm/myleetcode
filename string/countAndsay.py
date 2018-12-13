class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result='1'
        for i in range(n-1):
            result=self.count(result)
        return result
    def count(self, string):
        res=''
        result=''
        num=0
        for char in string:
            if char==res:
                num+=1
            else:
                if num:
                    result+=str(num)+res
                res=char
                num=1
        result+=str(num)+res
        return result

class Solution2(object):
    def countAndsay(self,n):
        result = '1'
        for i in xrange(n-1):
            result = self.count(result)
        return result
    def count(self, string):    
        res = ''
        result = ''
        num = 0
        for char in string:
            if char == res:
                num+=1
            else:
                if num:
                    result+=str(num)+res
                res=char
                num=1
        result+=str(num) + res
        return result

