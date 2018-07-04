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
