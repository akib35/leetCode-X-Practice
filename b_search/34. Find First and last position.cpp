#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> searchRange(vector<int> &nums, int target) {
    int left = 0, right = nums.size() - 1;
    vector<int> result = {-1,-1};
    if (nums.size() == 0) return result;
    while ( left < right ) {
      int mid = left + (right - left) / 2;
      if (nums[mid] < target) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    if (nums[left] != target) return result;
    result[0] = left;
    right = nums.size() - 1;
    while ( left < right ) {
      int mid = left + (right - left) / 2 + 1;
      if (nums[mid] > target) {
        right = mid - 1;
      } else {
        left = mid;
      }
    }
    result[1] = right;
    return result;    
  }
};

void runTests() {
  Solution sol;
  vector<int> input = {5,7,7,8,8,10};
  vector<int> expectedOutput = {3,4};
  assert(sol.searchRange(input, 8) == expectedOutput);
}

int main() {
  runTests();
  cout << "All tests passed!" << endl;
  return 0;
}
