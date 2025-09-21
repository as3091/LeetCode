# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.carry = False

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # try: 
        #     self.output
        # except:
        #     pass
        sum = 1 if self.carry else 0
        if l1:
            sum+= l1.val
            l1=l1.next
        if l2:
            sum+= l2.val
            l2=l2.next
        if sum>9:
            item = sum-10
            self.carry = True
        else:
            self.carry = False
            item = sum
        new_node = ListNode(item)
        if l1 or l2 or self.carry:
            new_node.next = self.addTwoNumbers(l1 = l1, l2 = l2)
        else:
            new_node.next = None
        return new_node
    
def linked_list_maker(input_list):
    LL_head = ListNode(input_list[0])
    current_node = LL_head
    for item in input_list[1:]:
        # Create a new node
        new_node = ListNode(item)
        # Link the current node to the new node
        current_node.next = new_node
        # Move the current node pointer forward
        current_node = new_node
    return LL_head

def linked_list_printer(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":

    # l1 = [9,9,9,9,9,9,9]
    # l2 = [9,9,9,9]
    l1 = [0]
    l2 = [0]
    L_1 = linked_list_maker(l1)
    linked_list_printer(L_1)
    L_2 = linked_list_maker(l2)
    linked_list_printer(L_2)

    sol_obj = Solution()
    sol_head = sol_obj.addTwoNumbers(L_1, L_2)
    linked_list_printer(sol_head)