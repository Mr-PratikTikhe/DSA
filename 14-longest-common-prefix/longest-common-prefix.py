class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        temp = strs[0]

        for word in strs[1:]:
            result = ""

            for i in range(min(len(temp), len(word))):
                if temp[i] == word[i]:
                    result += word[i]
                else:
                    break

            temp = result

            if temp == "":
                return ""

        return temp