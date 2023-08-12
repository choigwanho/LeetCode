class Solution {
    public void sortColors(int[] nums) {
        int cntR = 0; 
        int cntW = 0;
        
        for (int i = 0; i < nums.length; i++){
            if(nums[i]==0) cntR++;
            if(nums[i]==1) cntW++;
        }
        
        
        for (int i = 0; i < nums.length; i++){
            if(i < cntR) nums[i] = 0;
            if(cntR <= i && i < cntR+cntW) nums[i] = 1;
            if(cntR+cntW <= i)  nums[i] = 2;
        }
    }
}