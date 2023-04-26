# 作者：shu qi
# 开发时间：2022/7/21 11:14
'''该答案搬运 leetcode 喜欢吃番茄'''
class Solution:
    def canConstruct(self,ransomNote:str,magazine:str)->bool:
        ind=0
        m=magazine
        while True:
            if ind>len(ransomNote)-1:
                return True
            ch=ransomNote[ind]
            if ch in m:
                ind+=1
                m=m.replace(ch,'',1)
            else:
                return False
ransomNote=input("ransomNote:")
magazine=input("magazine:")
Solution.canConstruct(ransomNote,magazine)