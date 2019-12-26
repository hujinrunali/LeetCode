#题目描述：
# 最后一个单词的长度。
# 如果不存在最后一个单词，请返回 0 。
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
#
# 示例:
#
# 输入: "Hello World"
# 输出: 5
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split(' ')
        datalen = len(s)
        if datalen == 0:
            return 0
        tmpstr = s[-1]
        return len(tmpstr)