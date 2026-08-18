class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            
            if c == ')' or c == '}' or c == ']':
                if len(stack) == 0:
                    return False
                
                top = stack.pop()
                if not self.isClosed(top, c):
                    return False
        
        if len(stack) > 0:
            return False
        else:
            return True

    def isClosed(self, a:str, b:str) -> bool:
        if a=='(' and  b==')':
            return True
        if a=='{' and b=='}':
            return True
        if a=='[' and b== ']':
            return True
        return False 