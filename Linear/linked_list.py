"""
Linked list is a dynamic linear data structure that contains Nodes.
Each node contains : 1. Value of the node    2. Address of the next node
It mainly contains two pointers, head -> points first node, tail -> points last node.
"""

## Node class
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data): # ----->>>> Insert at the last of the linked list
        new_node = Node(data)
        
        ## Check fo empty
        if self.head == None:
            self.head = new_node
            print("Node inserted sucessfully")
            return

        else:
            temp  = self.head

            while temp.next != None:
                temp = temp.next
            
            temp.next = new_node
            print("Node inserted sucessfully")

    def insert_at_middle(self,value,pos):
        new_node = Node(value)

        ## Check if list is empty
        if self.head == None:
            new_node.next = self.head
            self.head = new_node
            print("Node inserted sucessfully")
            return
        
        else:
            curr = self.head
            prev = None
            i= 0 
            while i < pos:
                prev = curr
                curr = curr.next
            i += 1

            prev.next = new_node
            new_node.next = curr
            print("Node Inserted Succesfully")
            return

    def delete_from beginning(self):
        
        if self.head == None:
            print("Empty Linked List")
        
        else: 
            self.head = self.head.next

    def delete_from_end(self):

        ## Check for empty list
        if self.head == None:
            print("Empty Linked List")
            return

        ## Check for List with single node
        elif self.head.next == None:
            self.head = None
            print("Node Deleted Sucessfully")
            return

        else:
            temp = self.head
            while temp.next.next == None:
                temp = temp.next

            temp.next = None

    def delete_from_position(self,pos):
         
        ## Check for empty list
        if self.head == None:
            print("Empty Linked List")
            return
        
        ## Check for list with one node
        elif self.head.next = None:
            self.head = None
            print("Node Deleted Sucessfully")
            return

        else:
            

        



node1 = Node(10)
print(node1.data)
print(node1.next)