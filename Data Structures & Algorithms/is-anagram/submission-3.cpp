class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> v(26, 0);
        for(const char& c : s) v[c - 'a']++;
        for(const char& c : t) v[c - 'a']--;
        cout << v['x' - 'a'] << endl;
        for(const int& e : v) if (e != 0) return false;
        return true;
    }
};
