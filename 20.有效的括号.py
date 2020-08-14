class Solution:
    def isValid(self, s):

        # 核心思想
        # 直接判断字符串是否有连续的括号，有则替换为空
        # 最终判断s是否为空

        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''
    


    def isValid2(self, s: str) -> bool:

        # 核心思想--栈
        # 将s中的元素依次入栈，当循环到的元素与栈顶元素匹配
        # 则将栈顶元素出栈，若最终栈为空，则说明每一个括号都有匹配的，返回true

        if s == '':
            # 若s为空，直接返回true
            return True

        stack = list()
        n = len(s)
        stack.append(s[0])

        if n%2:
            # 若s的长度不是2的倍数则直接返回false
            # 因为括号必须成双成对出现
            return False

        for i in range(1, n):
            if stack ==  []:
                # 若stack中元素匹配完成后为空，则下个元素必须入栈
                stack.append(s[i]) 
            else:
                # 判断是否和栈顶元素配对
                if stack[-1] == '(' and s[i] == ')':
                    stack.pop()
                elif stack[-1] == '[' and s[i] == ']':
                    stack.pop()
                elif stack[-1] == '{' and s[i] == '}':
                    stack.pop()
                else:
                    # 若没不和栈顶元素配对，则入栈                
                    stack.append(s[i])        

        return stack == []