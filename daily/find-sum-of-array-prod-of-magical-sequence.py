# I am not that much good enough YET to understnd and solve this problem
# So lets copy one and call it a day
MOD = 10**9 + 7
from functools import lru_cache
import math


class Solution:
    def magicalSum(self, total_count: int, target_odd: int, numbers: list[int]) -> int:
        @lru_cache(None)
        def dfs(remaining: int, odd_left: int, i: int, carry: int) -> int:
            # Base cases
            if (
                remaining < 0
                or odd_left < 0
                or remaining + carry.bit_count() < odd_left
            ):
                return 0
            if remaining == 0:
                # Check if the number of odd bits in carry matches the target
                return 1 if carry.bit_count() == odd_left else 0
            if i == len(numbers):
                return 0

            total = 0
            # Try taking 0 to 'remaining' elements from numbers[i]
            for count in range(remaining + 1):
                ways = math.comb(remaining, count) * pow(numbers[i], count, MOD) % MOD
                new_carry = carry + count
                # Subtract 1 if new_carry is odd
                odd_adjust = new_carry % 2
                total += ways * dfs(
                    remaining - count, odd_left - odd_adjust, i + 1, new_carry // 2
                )
                total %= MOD

            return total

        return dfs(total_count, target_odd, 0, 0)
