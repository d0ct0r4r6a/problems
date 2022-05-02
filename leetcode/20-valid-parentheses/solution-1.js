/**
 * https://leetcode.com/submissions/detail/689580318/
 * 279 ms
 * 51.1 MB
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let parentheses = s.split("");
  let stack = [];
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
        stack.push(parenthesis);
      }
    }
  });
  return stack.length === 0;
};

let s = "]";
console.log(isValid(s));
