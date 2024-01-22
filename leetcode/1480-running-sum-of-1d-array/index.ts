function runningSum(nums: number[]): number[] {
  const sums = [nums[0]]
  for (let i = 1; i < nums.length; i++) {
      sums.push(sums[i - 1] + nums[i])
  }
  return sums
};