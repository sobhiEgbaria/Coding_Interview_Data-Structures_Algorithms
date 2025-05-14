// Given an integer array nums,
// move all 0's to the end of it while maintaining the relative order of the non-zero elements.

// Note that you must do this in-place without making a copy of the array.

// Example 1:
// Input: nums = [0,1,0,3,12]
// Output: [1,3,12,0,0]
// Example 2:

// Input: nums = [0]
// Output: [0]

const moveZeroes = (nums) => {
  let counter = 0;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] != 0) {
      nums[counter] = nums[i];
      counter++;
    }
  }
  let countOfZeros = nums.length - counter;
  for (let i = 0; i < countOfZeros; i++) {
    nums[nums.length - 1 - i] = 0;
  }

  return nums;
};

console.log(moveZeroes([0, 1]));
