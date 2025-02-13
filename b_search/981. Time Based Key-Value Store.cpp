#include <iostream>
#include <unordered_map>
#include <utility>
#include <vector>
#include <string>

using namespace std;

int main() {
    // Example usage
    Solution solution;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = solution.twoSum(nums, target);
    for (int i : result) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}

class TimeMap {
public:
    unordered_map<string ,vector<pair<int,string>>> data;
    
    TimeMap() {}
    
    void set(string key, string value, int timestamp) {
            data[key].emplace_back(timestamp,value);
        }
    
    string get(string key, int timestamp) {
      if (data.find(key) == data.end()) return "";
      
      auto& arr = data[key];
      int left = 0, right = arr.size();
      while (left < right) {
        int mid = left + (right - left) / 2;
        if (arr[mid].first <= timestamp) {
          left = mid + 1;
        } else {
          right = mid;
        }
      }
      return left == 0 ? "" : arr[left - 1].second;
      
    }
};
