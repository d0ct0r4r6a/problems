/**
 * https://leetcode.com/submissions/detail/689608975/
 * 87 ms
 * 42.6 MB
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  if (s.length === 1) {
    return false;
  } else if (s.length === 2) {
    return s === "{}" || s === "()" || s === "[]";
  } else if (s.length % 2 === 1) {
    return false;
  }
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
        return;
      }
    }
  });
  return stack.length === 0;
};

let s = "(]";
console.log(isValid(s));
