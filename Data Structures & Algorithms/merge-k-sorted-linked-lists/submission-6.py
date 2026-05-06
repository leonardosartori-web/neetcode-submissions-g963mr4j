# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        curr = res

        while True:
            minVal = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if minVal == -1 or lists[minVal].val > lists[i].val:
                    minVal = i
            if minVal == -1:
                break
            curr.next = lists[minVal]
            lists[minVal] = lists[minVal].next
            curr = curr.next
        return res.next
        