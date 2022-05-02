/**
 * https://leetcode.com/problems/valid-parentheses/discuss/482925/javascript/1032689
 * 64 ms
 * 42 MB
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  if (s.length == 0 || s.length % 2 != 0) {
    return false;
  }

  const closingParentheses = Object.freeze({
    "(": ")",
    "{": "}",
    "[": "]",
  });

  const stack = [];

  for (let i = 0; i < s.length; i++) {
    if (s[i] in closingParentheses) {
      stack.push(s[i]);
    } else if (s[i] != closingParentheses[stack.pop()]) {
      return false;
    }
  }

  return stack.length == 0;
};

let s = "(]";
console.log(isValid(s));
