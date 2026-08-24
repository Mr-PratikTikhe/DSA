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





# -------------------- HOW I DEVELOPED THIS --------------------
#
# 1. First, I understood that the input is a list of strings.
#
#    ["flower", "flow", "flight"]
#
# 2. I took the first string as the initial reference:
#
#    temp = "flower"
#
# 3. I learned that strings can be accessed character by character
#    using indexes:
#
#    "flower"[0] -> "f"
#    "flower"[1] -> "l"
#
# 4. I compared the same character positions between two strings:
#
#    flower
#    flow
#    ↑
#    f == f
#
#    l == l
#    o == o
#    w == w
#
#    Therefore:
#
#    result = "flow"
#
# 5. Then I used that result as the new temp and compared it with
#    the next string:
#
#    flow
#    flight
#
#    f == f
#    l == l
#    o != i
#
#    Therefore:
#
#    temp = "fl"
#
# 6. I repeated this process for every string until all strings
#    had been compared.
#
#
# -------------------- WHY min() IS USED --------------------
#
# Different strings can have different lengths.
#
# Example:
#
#    temp = "flower"
#    word = "flow"
#
# "flower" has length 6 but "flow" has length 4.
#
# Therefore:
#
#    range(min(len(temp), len(word)))
#
# only compares indexes 0 to 3.
#
# Without min(), trying to access word[4] would cause:
#
#    IndexError: string index out of range
#
#
# -------------------- TIME COMPLEXITY --------------------
#
# Let:
#
#    n = number of strings
#    m = length of the shortest string
#
# In the worst case, we compare up to m characters for each
# of the n strings.
#
# Time complexity:
#
#    O(n * m)
#
#
# -------------------- SPACE / MEMORY --------------------
#
# The algorithm uses extra space for "result" and "temp".
#
# Each time a matching character is added:
#
#    result += word[i]
#
# Python creates a new string because strings are immutable.
#
# For example:
#
#    ""
#    "f"
#    "fl"
#    "flo"
#    "flow"
#
# These string operations create temporary string objects.
#
# Therefore the extra space is approximately:
#
#    O(m)
#
# where m is the length of the common prefix.
#
# This is probably why the memory ranking is not as high as the
# runtime ranking on LeetCode.
#
#
# -------------------- LEETCODE RESULT --------------------
#
# Runtime: 0 ms
# Beats: 100%
#
# Memory: 19.37 MB
# Beats: 31.63%
#
# The runtime result is excellent, but LeetCode's runtime numbers
# can vary between runs because of the measurement environment.
#
# The memory result is acceptable, but there are solutions that
# use less additional memory.
#
# -------------------- IMPORTANT LESSON --------------------
#
# The main thing learned from this problem was not just the final
# code. The problem-solving process was:
#
#    Understand the problem
#           ↓
#    Break it into smaller parts
#           ↓
#    Compare characters using indexes
#           ↓
#    Build the common prefix
#           ↓
#    Repeat for every string
#           ↓
#    Handle edge cases
#           ↓
#    Optimize / analyze complexity
