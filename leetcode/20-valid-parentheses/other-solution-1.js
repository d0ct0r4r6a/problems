/**
 * https://leetcode.com/problems/valid-parentheses/discuss/482925/javascript/429779
 * 102 ms
 * 47.6 MB
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  while (
    s.indexOf("{}") !== -1 ||
    s.indexOf("[]") !== -1 ||
    s.indexOf("()") !== -1
  ) {
    s = s.replace("()", "");
    s = s.replace("{}", "");
    s = s.replace("[]", "");
  }
  return s === "";
};

let s = "(]";
console.log(isValid(s));
