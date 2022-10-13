#Leetcode question 141 https://leetcode.com/problems/linked-list-cycle/submissions/

#approach 1 - traverse and check in visited
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        temp = head
        while(temp):
            if(temp in visited):
                return True
            visited.append(temp)
            temp = temp.next
        return False
      
#approach 2 - pointer one jumps by 1 and pointer 2 jumps by 2
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp1 = head
        temp2 = head
        while(head!= None and temp1.next != None and temp2.next != None and temp2.next.next!=None):
            temp1 = temp1.next
            temp2 = temp2.next.next
            if(temp1 == temp2):
                return True
        return False
#approach 3 - hare and tortoise with the idea - "Apologize rather than asking persmission - use except instead of checking condition using if "
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head is None or head.next is None):
            return False
        tortoise = head
        hare = head.next
        while tortoise is not hare:
            try:
                tortoise = tortoise.next
                hare = hare.next.next
            except:
                return False
        return True
