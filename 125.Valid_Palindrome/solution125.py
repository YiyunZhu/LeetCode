class Solution: 
    def isPalindrome(self, s):
        new_s = []
        for c in s:
            #想了很多方法去除除了字母数字以外的符号，结果python一句话搞定，真的强大
            if c.isalnum():
                new_s.append(c.lower())
        return str(new_s)==str(new_s)[::-1]
            
        # After removing spaces and other characters
        # solution 1
        # a = len(s)
        # i = 0 
        # while i <= (a/2):
        #     if s[i] == s[a-i-1]:
        #         i += 1
        #         return True
        #     else:
        #         return False

        # solution 2
        # return str(s)==str(s)[::-1]

        # solution 3
        # a = reversed(list(s))
        # if list(a)==list(s):
        #     return True
        # return False

        # #40ms 大神的答案
        # if len(s) <= 1:
        #     return True
        
        # s = s.lower()
        # i = 0
        # j = len(s) - 1
        # while i <= j:
        #     while i <= j and not s[i].isalnum():
        #         i += 1
                
        #     while j >= i and not s[j].isalnum():
        #         j -= 1
            
        #     if i > j:
        #         break
                
        #     if s[i] != s[j]:
        #         return False
            
        #     i += 1
        #     j -= 1
        
        # return True

        