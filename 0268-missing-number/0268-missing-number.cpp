class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int len = nums.size();
        int missingNum =0;
        for(int i=0;i<=len;i++)
            missingNum ^= i;
        for(int i=0;i<len;i++)
            missingNum ^= nums[i];
        return missingNum;
    }
    
};