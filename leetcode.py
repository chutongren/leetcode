# 1071. 字符串的最大公因子
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # WHY range(min(len(str1), len(str2)),0, 1)), NOT START FROM 1
        # [) range(), array[]
        # 从，长度上的最大值，开始
        for i in range(min(len(str1), len(str2)),0, -1): 
            # 长度上也要既能除尽它，又能除尽它
            # 是%，不是//，%看能否除尽，是不是整数倍，长度是不是整数倍
            if(len(str1) % i == 0 and len(str2) % i == 0):
            # 取数  重复个数/次数
            # 想法先取str1各部分试，再str2，但最后要找的x如果在str2存在，str1必存在
            # x的开始是固定的，一定是str1的第一个
            # so，这道题重点就是长度上的要求，然后从str1的index=0开始取就完事
                if(str1[:i] * (len(str1)//i) == str1 and str1[:i] * (len(str2)//i) == str2): # 每次对两个字符串做拼接和比较，耗时 O(len1 + len2)
                    return str1[:i]
        return ''



# 1207. 独一无二的出现次数
# 每个数的出现次数都是独一无二的，而不是 每个数都是独一无二的
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num = Counter(arr).values() # count
        return len(set(num)) == len(num) # set去掉了重复的元素后，长度还是不变，说明无重复
