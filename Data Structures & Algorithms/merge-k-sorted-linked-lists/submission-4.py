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



        '''n = len(lists)
        if n == 0:
            return None
        elif n == 1:
            return lists[0]

        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]):
            if not list1 and not list2:
                return None
            elif list1 and not list2:
                list1.next = mergeTwoLists(list1.next, list2)
                return list1
            elif not list1 and list2:
                list2.next = mergeTwoLists(list1, list2.next)
                return list2
            else:
                if list1.val < list2.val:
                    list1.next = mergeTwoLists(list1.next, list2)
                    return list1
                else:
                    list2.next = mergeTwoLists(list1, list2.next)
                    return list2   
        
        times = len(lists)-1
        while times > 0:
            lists[0] = mergeTwoLists(lists[0], lists[times])
            times -= 1
        return lists[0]'''