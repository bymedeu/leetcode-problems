class Solution {
public:
    int minimumPushes(string word) {
        int s = word.length();
        if (s <  8)
            return s;
        vector<int> hist(26, 0);
        for (auto& ch : word)
        {
            hist[ch - 'a']++;
        }
        sort(hist.begin(), hist.end(), std::greater<>());
        int res= 0;
        for (int i = 0; i < 26; ++i)
        {
            if (hist[i] == 0)
                return res;
            res += hist[i] * (1 + (i / 8));
        }
        return res;
    }
};