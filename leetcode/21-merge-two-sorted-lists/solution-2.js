/**
 * https://leetcode.com/submissions/detail/689623676/
 * 86 ms, faster than 56.72%
 * 44.1 MB, less than 67.45%
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
  let combinedList = [];
  while (list1) {
    combinedList.push(list1.val);
    list1 = list1.next;
  }
  while (list2) {
    combinedList.push(list2.val);
    list2 = list2.next;
  }
  combinedList.sort((a, b) => a - b);
  combinedList = combinedList.map((val) => new ListNode(val, null));
  for (let i = 0; i <= combinedList.length - 2; i++) {
    combinedList[i].next = combinedList[i + 1];
  }

  if (combinedList.length) {
    return combinedList[0];
  } else {
    return null;
  }
};
