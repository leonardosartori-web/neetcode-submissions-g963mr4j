class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> s;
        for(const int& e : nums) {
            if (s.find(e) != s.end()) return true;
            s.insert(e);
        }
        return false;
    }
};
