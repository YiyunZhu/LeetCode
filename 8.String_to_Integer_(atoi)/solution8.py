class Solution:
    def atoi(self, str):
        str=str.strip()
        a=''
        if len(str)==0:
            return 0
        if len(str)==1 and str not in "0123456789":
            return 0
        if str[0] in "+-0123456789":
            a +=str[0]
        else:
            return 0
        if str[0] in "+-" and str[1] not in "0123456789":
            return 0
        for i in range(1,len(str)):
            if str[i].isdigit():
                a +=str[i]
            else:
                break
        a = int(a)
        a = a if a <= 2147483647 else 2147483647
        a = a if a >= -2147483648 else -2147483648
        return a

    #solution2
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        try:
            res = re.search('(^[\+\-]?\d+)', str).group()
            res = int(res)
            res = res if res <= 2147483647 else 2147483647
            res = res if res >= -2147483648 else -2147483648
        except:
            res = 0
        return res

    #solution3
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        str = str.strip()
        number, flag = 0, 1
        if str[0] == '-':
            str = str[1:]
            flag = -1
        elif str[0] == '+':
            str = str[1:]
        for c in str:
            if c >= '0' and c <= '9':
                number = 10*number + ord(c) - ord('0')
            else:
                break
        number = flag * number
        number = number if number <= 2147483647 else 2147483647
        number = number if number >= -2147483648 else -2147483648
        return number    