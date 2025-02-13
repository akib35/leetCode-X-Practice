#include <vector>
#include <map>

class SnapshotArray {
public:
    SnapshotArray(int length) {
        data.resize(length);
        snap_id = 0;
    }
    
    void set(int index, int val) {
        data[index][snap_id] = val;
    }
    
    int snap() {
        return snap_id++;
    }
    
    int get(int index, int snap_id) {
        auto it = data[index].upper_bound(snap_id);
        if (it == data[index].begin()) return 0;
        return prev(it)->second;
    }

private:
    std::vector<std::map<int, int>> data;
    int snap_id;
};


