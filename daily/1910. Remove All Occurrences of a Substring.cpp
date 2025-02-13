#include <iostream>
#include <string>

class Solution {
public:
    std::string removeOccurrences(std::string s, std::string part) {
      size_t position = s.find(part);
      while (position != std::string::npos) {
        s.erase(position, part.size());
        position = s.find(part);
      }
      return s;
    }
};

int main() {
    Solution solution;
    std::string s = "daabcbaabcbc";
    std::string part = "abc";
    std::cout << solution.removeOccurrences(s, part) << std::endl;
    return 0;
}