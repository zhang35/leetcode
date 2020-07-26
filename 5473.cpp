class Solution {
public:
    int minFlips(string s) {
        s = "0"+s;
        int res = 0;
        for (int i = 1; i < s.size(); ++i)
            if (s[i] != s[i-1]) ++res;
        return res;
    }
};

