class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Stack for adding parenthesis

        # Iterate through the entire string
        for p in s:
            if p == "[" or p == "{" or p == "(":
                stack.append(p)
            elif p == "]" or p == "}" or p == ")":
                if stack == []: return False  # Edge case of empty list
                preceding = stack.pop()
                # If parenthesis are not equal, return False
                if preceding == "[" and p != "]":
                    return False
                elif preceding == "{" and p != "}":
                    return False
                elif preceding == "(" and p != ")":
                    return False

        # All cases passed, return true
        return len(stack) == 0