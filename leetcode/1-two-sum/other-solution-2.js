// https://leetcode.com/problems/two-sum/discuss/1894284/JavaScript-code
// 258 ms
// 42.2 MB
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const num = [];
  var l = nums.length;
  for (i = 0; l - 1; i++) {
    x = nums[i];
    y = target - x;
    if (nums.includes(y)) {
      num[0] = i;
      num[1] = nums.indexOf(y);
      if (num[1] != num[0]) {
        break;
      }
    }
  }
  return num;
};

let nums, target;
(nums =[3, 3]), (target = 6);
console.log(twoSum(nums, target));
