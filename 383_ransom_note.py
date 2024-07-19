class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = [x for x in magazine]
        for each in ransomNote:
            try:
                mag.remove(each)
            except:
                return False
        
        return True

