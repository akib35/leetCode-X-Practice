class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if self.isPalindrome(s):
            return s

        for i in range(len(s)):
            print(s[:len(s) - i])
            if self.isPalindrome(s[:len(s) - i]):
                return s[len(s) - i:][::-1] + s

        return ""

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]


def main():
    solution = Solution()
    print(solution.shortestPalindrome("aacecaaa"))  # Output: "aaacecaaa"
    print(solution.shortestPalindrome("abcd"))      # Output: "dcbabcd"

if __name__ == "__main__":
    main()
