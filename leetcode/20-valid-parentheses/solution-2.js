/**
 * https://leetcode.com/submissions/detail/689600846/
 * 78 ms
 * 44 MB
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let parentheses = s.split("");
  let stack = [];
  let result = true;
  parentheses.forEach((parenthesis) => {
    if (["(", "[", "{"].includes(parenthesis)) {
      stack.push(parenthesis);
    } else {
      let stackTopElement = stack[stack.length - 1];
      if (
        (parenthesis === ")" && stackTopElement === "(") ||
        (parenthesis === "]" && stackTopElement === "[") ||
        (parenthesis === "}" && stackTopElement === "{")
      ) {
        stack.pop();
      } else {
        result = false;
        return;
      }
    }
  });
  return stack.length === 0 && result;
};

let s = "(]";
console.log(isValid(s));
