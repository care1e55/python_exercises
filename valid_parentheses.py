
class Solution:

    brackets = {
        "[": "]", 
        "{": "}", 
        "(": ")"
        }

    def isValid(self, s: str) -> bool:
        stack = list()
        for bracket in s:
            if bracket in self.brackets:
                stack.append(self.brackets[bracket])
            else:
                if stack and bracket == stack.pop():
                    continue
                return False
        if not stack:
            return True
        return False



if __name__ == '__main__':
    test_str_1 = "()"
    test_str_2 = "()[]{}"
    test_str_3 = "(]"
    test_str_4 = "([])"
    test_str_5 = "["
    test_str_6 = "]"

    assert Solution().isValid(test_str_1) == True
    assert Solution().isValid(test_str_2) == True 
    assert Solution().isValid(test_str_3) == False
    assert Solution().isValid(test_str_4) == True
    assert Solution().isValid(test_str_5) == False
    assert Solution().isValid(test_str_6) == False
    
    print('Solution is OK')

