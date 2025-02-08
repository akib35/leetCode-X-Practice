#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int firstBadVersion(int n) {
    int left = 1, right = n;
    while (left < right) {
      int mid = left + (right - left) / 2;
      if (isBadVersion(mid)) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }
    return left;
  }
};

int main() {
  Solution solution;
  int nums = 5;
  int result = solution.firstBadVersion(nums);

  cout << "Result: " << result << endl;

  return 0;
}
