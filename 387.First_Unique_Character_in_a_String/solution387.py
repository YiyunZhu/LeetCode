class Solution:
    def firstUniqChar(self, s):
        #     # #It works but for long string, time limited exceeded
    #     # for i in range(len(str)):
    #     #     while str.count(str[i])==1:
    #     #         return i
    #     # return -1
        ch=[]
        for i in set(s):
            if s.count(i) == 1:
                ch.append(s.index(i))
        if len(ch)>0:
            return min(ch)
        else:
            return -1

    
    
def main():
    # input="dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    s="absd"
    print(Solution().firstUniqChar(s))
    
    
if __name__ == '__main__':
    main()
