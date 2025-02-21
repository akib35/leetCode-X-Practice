#include <vector>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        auto it = lower_bound(matrix.begin(), matrix.end(), vector<int>{target}, [](const vector<int>& row, const vector<int>& val) {
            return row.back() < val[0];
        });
        if (it == matrix.end()) return false;
        return binary_search(it->begin(), it->end(), target);
    }
};