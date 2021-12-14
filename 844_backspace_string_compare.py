class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.removeBackspace(s) == self.removeBackspace(t)


    def removeBackspace(self, s: str):
        while '#' in s:
            index = s.index('#')
            if index == 0:
                s = s[1:]
            else:
                s = s[:index-1] + s[index+1:]
        return s
