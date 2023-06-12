# *******************************************************************************
# Question
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:


# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# *******************************************************************************
# Solution
# 1. Initialize a variable temp to head, which is the head of the linked list. This variable will be used to traverse the linked list.
# 2. Enter a while loop that checks two conditions: temp is not None and temp.next is not None. This loop will continue until temp reaches the last node or the second last node of the linked list.
# 3. Inside the while loop, update head by moving it one node forward using head = head.next. This effectively moves head towards the middle of the linked list by one step in each iteration.
# 4. Update temp by moving it two nodes forward using temp = temp.next.next. This effectively moves temp towards the end of the linked list by two steps in each iteration.
# 5. When the while loop exits, it means that temp has reached the last node or the second last node, and head is at the middle node of the linked list.
# 6. Return the value of head, which represents the middle node or the second middle node of the linked list.

class Solution(object):
    def middleNode(self, head):
        temp = head
        while temp and temp.next:
            head = head.next
            temp = temp.next.next
        return head
    
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# create the linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()

result = solution.middleNode(head)

while result:
    print(result.val)
    result = result.next
    
# Time Complexity :  O(n)
# Space Complexity : O(1)