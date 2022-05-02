/**
 * https://leetcode.com/submissions/detail/689620487/
 * 109 ms, faster than 25.54%
 * 44.2 MB, less than 56.05%
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
  let mergedList, mergedListHead;
  if (list1 && list2) {
    if (list1.val >= list2.val) {
      mergedListHead = list2;
      mergedList = list2;
      list2 = list2.next;
    } else {
      mergedListHead = list1;
      mergedList = list1;
      list1 = list1.next;
    }
  } else if (list1) {
    mergedListHead = list1;
    mergedList = list1;
    list1 = list1.next;
  } else if (list2) {
    mergedListHead = list2;
    mergedList = list2;
    list2 = list2.next;
  } else {
    mergedListHead = null;
  }
  while (list1 || list2) {
    if (list1 && list2) {
      if (list1.val >= list2.val) {
        mergedList.next = list2;
        list2 = list2.next;
      } else {
        mergedList.next = list1;
        list1 = list1.next;
      }
    } else if (list1) {
      mergedList.next = list1;
      list1 = list1.next;
    } else {
      mergedList.next = list2;
      list2 = list2.next;
    }
    mergedList = mergedList.next;
  }
  return mergedListHead;
};
