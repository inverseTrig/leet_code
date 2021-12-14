class Solution:
    def entityParser(self, text: str) -> str:
        mapping = {"quot": "\"",
                   "apos": "\'",
                   "amp": "&",
                   "gt": ">",
                   "lt": "<",
                   "frasl": "/",
                   }

        splitted = text.split('&')
        final = splitted[0]
        for i in range(1, len(splitted)):
            if splitted[i] and ';' in splitted[i]:
                pre, suf = splitted[i].split(';', maxsplit=1)
                final += mapping.get(pre, '&' + pre + ';') + suf
            else:
                final += '&' + splitted[i]
        return final


sol = Solution()
print(sol.entityParser(text="&amp; is an HTML entity but &ambassador; is not."))
print(sol.entityParser(text="&&&amp&&"))
