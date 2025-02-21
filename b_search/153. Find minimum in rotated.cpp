#include <climits>
#include <vector>
using namespace std;

class Solution {
public:
  int findMin(vector<int> &nums) {
    int min = INT_MAX;
    int left = 0, right = nums.size() - 1;
    while (left <= right) {
      int mid = left + (right - left) / 2;
      min = min < nums[mid] ? min : nums[mid];
      if (nums[mid] > nums[left]) {
        min = min < nums[left] ? min : nums[left];
        left = mid + 1;
      } else {
        min = min < nums[right] ? min : nums[right];
        right = mid - 1;
      }
    }
    return min;
  }
};
