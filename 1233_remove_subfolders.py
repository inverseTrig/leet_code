class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folders = folder
        folders.sort()

        output = []
        parent = " "

        for f in folders:
            if not f.startswith(parent):
                output.append(f)
                parent = f + "/"

        return output
