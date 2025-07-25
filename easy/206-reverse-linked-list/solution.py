from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    @staticmethod
    def generate_from_array(array: List[int], index = 0):
        if not array:
            return None

        head = ListNode(array[0])
        current = head

        for e in array[1:]:
            current.next = ListNode(e)
            current = current.next

        return head

    @staticmethod
    def list_to_array(input_list: Optional) -> List[int]:
        array = []

        while input_list is not None:
            array.append(input_list.val)
            input_list = input_list.next

        return array
    

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head 
        previous = None
        next_node = None

        while current is not None: 
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
    
        # Previous has become the new current
        
        while previous is not None: 
            print(previous.val)
            previous = previous.next
                
        return previous



head = LinkedList.generate_from_array([1,2,3,4,5]) 
solutionLeet = Solution()
solutionLeet.reverseList(head)