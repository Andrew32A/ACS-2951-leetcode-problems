# *******************************************************************************
# Question
# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

# *******************************************************************************
# Solution
# To rotate a linked list to the right by k places, we need to perform the following steps:
# 1. Calculate the length of the linked list by traversing it and keeping a count of the number of nodes. Let's call this count variable "length".
# 2. If the length is 0 or 1, or if k is a multiple of length, the list remains unchanged. Return the head of the original linked list in such cases.
# 3. Calculate the actual number of rotations required using the formula: rotations = k % length. This will give us the effective number of rotations within a single cycle of the linked list.
# 4. If rotations is 0, the list remains unchanged. Return the head of the original linked list.
# 5. Move the pointer "fast" k steps ahead from the head of the linked list. If "fast" reaches the end of the list, wrap it back to the head.
# 6. Move both "fast" and "slow" pointers simultaneously until "fast" reaches the end of the list. This will ensure that "slow" reaches the node just before the new head of the rotated list.
# 7. Update the new head of the rotated list as "new_head = slow.next" and set "slow.next = None" to break the original linked list and form a new tail.
# 8. Connect the original tail to the original head, making it a circular linked list again.
# 9. Return the new head of the rotated list.

class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        
        rotations = k % length
        
        if rotations == 0:
            return head
        
        fast = slow = head
        for _ in range(rotations):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        new_head = slow.next
        slow.next = None
        tail.next = head
        
        return new_head


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Create the linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()

result = solution.rotateRight(head, 2)

while result:
    print(result.val)
    result = result.next

# Time Complexity: O(n)
# Space Complexity: O(1)