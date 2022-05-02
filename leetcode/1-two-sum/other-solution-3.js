// https://leetcode.com/problems/two-sum/discuss/493704/Simple-JavaScript-beats-98
// 48 ms
// 34 MB
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let dic = {};
  for (let i = 0; i < nums.length; i++) {
    if (target - nums[i] in dic) {
      return [dic[target - nums[i]], i];
    }
    dic[nums[i]] = i;
  }
};

let nums, target;
(nums = [3, 2, 4]), (target = 6);
console.log(twoSum(nums, target));
