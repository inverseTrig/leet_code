class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        odd_s1, even_s1, odd_s2, even_s2 = [], [], [], []

        for i, (s1_value, s2_value) in enumerate(zip(s1, s2)):
            if i % 2 == 0:
                even_s1.append(s1_value)
                even_s2.append(s2_value)
            else:
                odd_s1.append(s1_value)
                odd_s2.append(s2_value)
        
        odd_s1.sort()
        even_s1.sort()
        odd_s2.sort()
        even_s2.sort()

        return odd_s1 == odd_s2 and even_s1 == even_s2

