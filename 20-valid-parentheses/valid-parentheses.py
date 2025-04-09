class Solution:
    def isValid(self, s: str) -> bool:
        # use stack
        # ex: [()]
        #  add to stack if opening
        # if closing then pop latest in stack if it matches the corresponding type then good else false

        match = {
            '{':'}',
            '[':']',
            '(':')'
        }
        stack = []

        for e in s:
            # check next char
            
            # case 1: is opening, append
            if e in match:
                stack.append(e)
            # case 2: is closing, check top of stack
            elif len(stack) > 0:
                top = stack.pop()
                if e != match[top]:
                    return False
            # case 3: empty stack or ']' in stack
            else:
                return False
        
        if len(stack) != 0:
            return False
        return True

        

    