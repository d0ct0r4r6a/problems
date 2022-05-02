// https://leetcode.com/problems/two-sum/discuss/326/simple-Javascript-code
// 89 ms
// 43 MB
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let map = new Map();

  for (let i = 0; i < nums.length; i++) {
    let num = nums[i];
    if (map.get(num) === undefined) map.set(target - num, i);
    else return [map.get(num), i];
  }
};

let nums, target;
(nums = [3, 2, 4]), (target = 6);
console.log(twoSum(nums, target));
