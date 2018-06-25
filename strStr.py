class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        f_len = len(haystack)
        s_len = len(needle)
        if s_len == 0 :
            return 0
        if s_len > f_len:
            return -1
        
        length = f_len - s_len + 1
        for i in range(length):
            if haystack[i:i+s_len] == needle:
                return i
        return -1
s = Solution()
ret = s.strStr('aalsdfkl','ll')
print ret
