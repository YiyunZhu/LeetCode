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
