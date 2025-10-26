class Solution:
    def isBalanced(self, s: str, i: int) -> bool:
        left_score = sum(ord(ch) - ord("a") + 1 for ch in s[: i + 1])
        right_score = sum(ord(ch) - ord("a") + 1 for ch in s[i + 1 :])
        print(left_score, right_score)
        return left_score == right_score

    def scoreBalance(self, s: str) -> bool:
        for i in range(len(s)):
            if self.isBalanced(s, i):
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.scoreBalance("adcb"))  # True
    print(s.scoreBalance("abdcd"))  # True
    print(s.scoreBalance("abc"))  # False
