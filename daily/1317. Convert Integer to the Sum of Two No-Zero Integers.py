class Solution:
    def get_no_zero_integers(self,n):
        digits = list(map(int, str(n)))[::-1]
        a_digits = []
        b_digits = []
        carry = 0

        for i in range(len(digits)):
            d = digits[i] + carry
            carry = 0

            if d < 2:
                d += 10
                carry = -1

            for d_a in range(1, 10):
                d_b = d - d_a
                if 1 <= d_b <= 9:
                    a_digits.append(d_a)
                    b_digits.append(d_b)
                    break
            else:
                raise ValueError("No valid split found")

        if carry == -1:
            # Add extra digit 1 to handle leftover borrow
            a_digits.append(1)
            b_digits.append(1)

        a = int(''.join(map(str, a_digits[::-1])))
        b = int(''.join(map(str, b_digits[::-1])))

        return [a, b]

sol = Solution()
print(sol.get_no_zero_integers(859))  # Expected something like [1, 858] or any valid no-zero pair
print(sol.get_no_zero_integers(1000)) # Expected [445, 555] or similar
print(sol.get_no_zero_integers(2))    # [1, 1]
print(sol.get_no_zero_integers(11))   # e.g. [5, 6]
