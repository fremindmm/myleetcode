class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.strip(' ') == '':
            return 0
        l = s.split(' ')
        for i in l[::-1]:
            if i:
                return len(i)

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = s.split(' ')
        while r[-1] == '' :
            r.pop()
            if len(r) == 0:return 0
        return len(r[-1])
