class Solution {
public:
    int minimumPushes(string word) {
        int res2 = word.length();
        int res = res2;
        cout << res;
        while (res2 > 8)
        {
            res += res2 - 8;
            res2-=8;
        }
        return res;
        

        
        
    }
};