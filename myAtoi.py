class Solution(object):
    def myAtoi(self, ss):
        """
        :type s: str
        :rtype: int
        """
        s = ss.strip()
        if s == '' or (len(s) == 1 and (not s[0].isdigit())):
            return 0
        if len(s) == 1 and s[0].isdigit():
            return int(s)
        sub_s = ''
        if (not s[0].isdigit()) and (s[0] not in ['+', '-']):
            return 0
        if (not s[0].isdigit()) and (s[0] in ['+', '-']):
            sub_s += s[0]
            if not s[1].isdigit():
                return 0
            sub_s += s[1]
            for i in range(2, len(s)):
                if s[i].isdigit():
                    sub_s += s[i]
                else:
                    break
        if s[0].isdigit():
            sub_s += s[0]
            for ii in range(1, len(s)):
                if s[ii].isdigit():
                    sub_s += s[ii]
                else:
                    break
        num = int(sub_s)
        if (num >= (-2 ** 31)) and (num <= (2 ** 31 - 1)):
            return num
        elif num < (-2 ** 31):
            return -2 ** 31
        else:
            return 2 ** 31 - 1

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        ret = re.findall(r"^[-+]?\d+",str.strip())
        if ret:
            ret_str = ret[0]
            tmp = ""
            if ret_str[0] == "-" or ret_str[0] == "+":
                tmp = ret_str[1:]
            else:
                tmp = ret_str
            ret_int = int(tmp)
            if ret_str[0] == '-':
                return -ret_int if ret_int <= 2**31 else -2**31
            else:
                return ret_int if ret_int < 2**31 else 2**31-1
        else:
            return 0
