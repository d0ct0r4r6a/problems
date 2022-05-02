// 2022-04-29
// 1036ms
// 73.6MB
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  return nums.reduce((prev, curr, ind) => {
    if ([...nums.slice(0, ind), ...nums.slice(ind + 1)].includes(target - curr)) {
      prev.push(ind);
    }
    return prev;
  }, []);
};
