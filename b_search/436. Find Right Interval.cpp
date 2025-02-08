#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> findRightInterval(vector<vector<int>> &intervals) {
    vector<int> result;
    vector<pair<int, int>> start;
    for (int i = 0; i < intervals.size(); i++) {
        start.push_back({intervals[i][0], i});
    }
    sort(start.begin(), start.end());
    for (int i = 0; i < intervals.size(); i++) {
        int target = intervals[i][1];
        int left = 0, right = start.size() - 1;
        int index = -1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (start[mid].first == target) {
                index = start[mid].second;
                break;
            } else if (start[mid].first < target) {
                left = mid + 1;
            } else {
                index = start[mid].second;
                right = mid - 1;
            }
        }
        result.push_back(index);
    }
    return result;
    
  }
};

int main() {
  Solution solution;
  vector<vector<int>> nums = {{3,4},{2,3},{1,2}};
  vector<int> result = solution.findRightInterval(nums);
  for (int i = 0; i < result.size(); i++) {
    cout << result[i] << " ";
  }
  return 0;
}
