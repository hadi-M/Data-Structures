from pdb import set_trace as st


"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    # def __repr__(self):
    #     return f"({self.prev}) <P-- [{self.value}] --N> ({self.next})"


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        old_head = self.head
        new_head = ListNode(value, prev=None, next=old_head)
        old_head.prev = new_head
        self.head = new_head
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 0:
            return None
            
        return_value = self.head.value

        new_head = self.head.next
        new_head.prev = None
        self.head = new_head

        self.lenght -= 1

        return return_value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        old_tail = self.tail
        new_tail = ListNode(value, prev=old_tail, next=None)
        old_tail.next = new_tail
        self.tail = new_tail
        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 0:
            return None

        return_value = self.tail.value

        new_tail = self.tail.prev
        new_tail.next = None
        self.tail = new_tail

        self.lenght -= 1

        return return_value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        next_node = node.next
        prev_node = node.prev
        st()

        if next_node is not None:
            next_node.prev = prev_node

        if prev_node is not None:
            prev_node.next = next_node

        # prev_node.prev = next_node

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current_node = self.head
        max_value = self.head.value

        while current_node.next is not None:
            max_value = current_node.value
            current_node = current_node.next

        return max_value

    """
    prints the list in a readable fashion
    """
    def print_list(self):
        current_node = self.head
        max_value = self.head.value

        while True:
            prev_value = None
            next_value = None
            if current_node.prev != None:
                prev_value = current_node.prev.value
            
            if current_node.next != None:
                next_value = current_node.next.value

            # st()
            print(f"({str(prev_value)}) <P-- [{current_node.value}] --N> ({str(next_value)})")
            # st()
            # self.dll.print_lis()
            current_node = current_node.next

            if current_node is None:
                break


if __name__ == "__main__":
    aa = DoublyLinkedList(ListNode(2))
    print("printing:")
    aa.print_list()
    print("Done printing \n\n")
    aa.add_to_head(4)
    print("printing:")
    aa.print_list()
    print("Done printing \n\n")
    aa.delete(aa.head)
    # st()