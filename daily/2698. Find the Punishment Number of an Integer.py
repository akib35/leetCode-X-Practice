class Solution:
    nums = [1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 379, 414, 657, 675, 703, 756, 792, 909, 918, 945, 964, 990, 991, 999, 1000]
    def punishmentNumber(self, n: int) -> int:
        sum = 0
        for i in range(len(self.nums)):
            if self.nums[i] <= n:
                sum += self.nums[i]**2
        return sum
    
def main():
    solution = Solution()
    punishment_numbers = solution.punishmentNumber(10)
    print(punishment_numbers)

if __name__ == "__main__":
    main()

# class Solution:
#     def punishmentNumber(self, n: int) -> int:
#         punishment_numbers = self.calculatePunishmentNumber(n)
#         return sum(punishment_numbers)  # Return the sum of punishment numbers

#     def calculatePunishmentNumber(self, n: int) -> list:
#         nums = []
#         for i in range(1, n + 1):  # Include n in the range
#             square = str(i * i)
#             if self.canPartition(square, i):
#                 nums.append(i)
#         return nums

#     def canPartition(self, square: str, target: int) -> bool:
#         # This function will check if we can partition the square into parts that sum to target
#         length = len(square)
        
#         # Generate all possible partitions
#         def backtrack(start: int, current_sum: int) -> bool:
#             if start == length:
#                 return current_sum == target
            
#             for end in range(start + 1, length + 1):
#                 part = int(square[start:end])  # Get the current part
#                 if backtrack(end, current_sum + part):
#                     return True
            
#             return False
        
#         return backtrack(0, 0)

# def main():
#     solution = Solution()
#     punishment_numbers = solution.calculatePunishmentNumber(1000)
#     print(punishment_numbers)

# if __name__ == "__main__":
#     main()