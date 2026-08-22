class Solution {
public:
    bool checkDivisibility(int n) {
        int x = n;
        int s = 0;
        int p = 1;
        while (x > 0)
        {
            s += x % 10;
            p *= x % 10;
            x /= 10;
        }
        return n % (s + p) == 0;
    }
};