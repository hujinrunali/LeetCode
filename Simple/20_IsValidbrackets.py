#题目描述：
#给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
# 示例 1:
# 输入: "()"
# 输出: true
# 示例 4:
# 输入: "([)]"
# 输出: false
#算法时间复杂度分析：O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        #解题思路：利用栈的数据结构，遇到左括号入栈，遇到右括号出栈
        #并进行比对
        left = ['(','[','{']
        right = [')',']','}']
        if s == '':
            return True
        stack = []
        for letter in s:
            if letter in left:
                stack.append(letter)
            if letter in right:
                #这个地方需要考虑stack为空的情况，这种时候括号也是不合格的
                if not stack:
                    return False
                else:
                    templetter = stack.pop()
                    if left.index(templetter) != right.index(letter):
                        return False
        if stack:
            return False
        return True