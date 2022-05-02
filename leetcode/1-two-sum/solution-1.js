// 2017-07-28
// 325ms
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
  result = [];
  for (i = 0; i < nums.length; i++) {
      for (j = (i+1); j < nums.length; j++) {
          if (nums[i] + nums[j] == target){
              result.push(i);
              result.push(j);
              return result;
          }
      }
  }
};
