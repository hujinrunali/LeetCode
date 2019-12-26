#题目描述：给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
#字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
class Solution:
    def findAnagrams(self, s, p):
        #特殊情形的判断
        if not s or not p:
            if not s and not p:
                return [0]
            else:
                return []
        left = right = 0
        match = 0
        needs = {}
        windows = {}
        res = []
        for c in p:
            needs[c] = needs.get(c,0)+1
        while right < s.__len__():
            c1 = s[right]
            windows[c1] = windows.get(c1,0)+1
            if c1 in needs and windows[c1] == needs[c1]:
                match += 1
            right += 1
            while match==needs.__len__():
                if right-left == p.__len__():
                    res.append(left)
                c2 = s[left]
                windows[c2] -= 1
                if c2 in needs and windows[c2] < needs[c2]:
                    match -= 1
                left += 1
        return res

if __name__ == "__main__":
    s = "baa"
    p = "aa"
    sl = Solution()
    print(sl.findAnagrams(s,p))
