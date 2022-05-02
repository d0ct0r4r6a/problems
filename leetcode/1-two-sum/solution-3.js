// 2022-04-29
// 677ms
// 42.7 MB
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let a, b;
  a = nums.findIndex((value, index) => {
    let pairingIndex = nums.findIndex(
      (val, ind) => target - value === val && ind !== index
    );
    if (pairingIndex >= 0) {
      b = pairingIndex;
      return true;
    }
  });
  return [a, b];
};

let nums, target;
(nums = [3, 2, 4]), (target = 6);
console.log(twoSum(nums, target));
