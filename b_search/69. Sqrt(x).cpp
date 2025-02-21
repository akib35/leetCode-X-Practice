class Solution {
public:
    int mySqrt(int x) {
      int lo = 0, hi = x/2;
      int mid;
      while (lo <= hi) {
        mid = lo + (hi - lo) / 2;
        if (mid == x / mid) return mid;
        if (mid < x / mid) lo = mid + 1;
        else hi = mid - 1;
      }
      return hi;
    }
};
//add this for better space optimization
int init = [] {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    ofstream out("user.out");
    cout.rdbuf(out.rdbuf());

    Solution s;
    for (string line; getline(cin, line); cout << endl)    
            cout << s.mySqrt(stoul(line));    
    exit(0);
    return 0;
}();