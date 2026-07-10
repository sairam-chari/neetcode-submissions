class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s=="":
            return True
        for i in s:
            if i == "(":
                stack.append(1)
            elif i == "[":
                stack.append(2)
            elif i == "{":
                stack.append(3)
            elif i == ")":
                if len(stack)==0 or stack.pop()!=1:
                    return False
            elif i == "]":
                if len(stack)==0 or stack.pop()!=2:
                    return False
            elif i == "}":
                if len(stack)==0 or stack.pop()!=3:
                    return False
        return True if len(stack)==0 else False