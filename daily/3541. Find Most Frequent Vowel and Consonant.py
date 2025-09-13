from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        chars = Counter(s)
        vowels = set('aeiou')
        maxVowelfreq, maxConsfreq = 0, 0

        for char,freq in chars.items():
            if char in vowels:
                maxVowelfreq = max(freq, maxVowelfreq)
            else:
                maxConsfreq = max(freq, maxConsfreq)

        return maxVowelfreq + maxConsfreq
