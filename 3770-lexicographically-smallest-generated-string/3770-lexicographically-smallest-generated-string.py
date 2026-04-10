class Solution:
    """
    def addWord(self, word: str, newWord : str, i : int, fixed : List[bool]) -> str:
        Ls = len(newWord)
        for j in range(Ls):
            if word[i + j] != ' ' and word[i + j] != newWord[j]:
                return ""
            if fixed:
                fixed[i] = True
        return word[:i] + newWord + word[i + Ls:]
        
    def repairWord(word : str, l : int, i : int, fixed : List[bool]):
        Ls = len(word)
        if i + m >= Ls:
            return ""
        for j in range(m):
            if fixed[i + m - j] == False:
                return self.addWord(word, "b", i + m - j, fixed)
        return ""
            
        
    
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        wordLen = n + m - 1

        word = " " * wordLen
        fixed = [False] * n
        
        for i in range(n):
            if str1[i] == "T":
                word = self.addWord(word, str2, i, fixed)
                if word == "":
                    return word
                i += m - 1
            else:
                word = self.addWord(word, "a", i, None)

        for i in range(n):
            if str1[i] == 'F':
                word = self.repairWord(word, m, i, fixed)
                if word == "":
                    return word
        
        return word
        """
    def generateString(self, str1: str, str2: str) -> str:

        n = len(str1)
        m = len(str2)
        wordLen = n + m - 1
        word = ['a'] * wordLen
        fixed = [False] * wordLen
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if fixed[i + j] and word[j + i] != str2[j]:
                        return ""
                    word[j + i] = str2[j]
                    fixed[j + i] = True

        for i in range(n):
            if str1[i] == "F":
                if any(str2[j - i] != word[j] for j in range(i, i + m)):
                    continue
                for j in range(i + m - 1, i - 1, -1):
                    if not fixed[j]:
                        word[j] = "b"
                        break
                else:
                    return ""
        return "".join(word)

"""
        First handle the 'T', make all required changes in the char array, and use a boolean array to mark locked positions (fixed by 'T'), if any conflict occurs return "". Then handle 'F', and if a substring matches str2, change one unlocked character to break it, iterating from right to left to keep the string lexicographically smallest. I hope this will help."""