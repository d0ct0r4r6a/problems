function kthDistinct(arr: string[], k: number): string {
  const counter = {}
  for (const str of arr) {
      if (str in counter) {
          counter[str]++
      } else {
          counter[str] = 1
      }
  }
  let i = 1;
  for (const str of arr) {
      if (i > k) {
          return ''
      }
      if (counter[str] == 1 && i == k) {
          return str
      }
      if (counter[str] == 1) {
          i++
      }
  }
  return ''
};