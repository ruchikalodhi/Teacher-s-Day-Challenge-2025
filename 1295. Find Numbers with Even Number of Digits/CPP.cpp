class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int count = 0;
        for (int num : nums) {
            if (isEven(num)) {
                count++;
            }
        }
        return count;
    }

private:
    bool isEven(int num) {
        int numOfDigit = noOfDigits(num);
        return numOfDigit % 2 == 0;
    }

    int noOfDigits(int num) {
        return (int)(log10(num)) + 1;
    }
};
