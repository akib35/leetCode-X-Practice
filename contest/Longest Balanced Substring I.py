from collections import Counter


class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_length = 0
        for i in range(n):
            for j in range(i, n):
                substring = s[i : j + 1]

                freq = Counter(substring)

                frequencies = list(freq.values())
                if len(set(frequencies)) == 1:
                    max_length = max(max_length, len(substring))

        return max_length
