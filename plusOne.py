class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in reversed(xrange(0,len(digits))):
            digit = (digits[i]+carry)%10
            carry = 1 if digit < digits[i] else 0#判断是否进位
            digits[i]=digit
        if carry == 1:
            return [1]+digits#如果依然进位，就1+后面的0
        return digits

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        intNum = 0
        for i in range(len(digits)):
            intNum = intNum*10+digits[i]
        intNum+=1
        strNum=str(intNum)
        ret=[]
        for i in strNum:
            ret.append(int(i))
        return ret

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits is None:
            return

        length = len(digits)
        for i in range(length - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str_num=''
        for i in digits:
            str_num+=str(i)
        ret = int(str_num)+1
        str_ret= list(str(ret))
        return [int(i) for i in str_ret]
