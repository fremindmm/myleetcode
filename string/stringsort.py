class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        from itertools import permutations
        if len(s1) > len(s2):
            return False                                         
        for i in permutations(s1):
            if ''.join(i) in s2:
                return True
        else:
            return False
