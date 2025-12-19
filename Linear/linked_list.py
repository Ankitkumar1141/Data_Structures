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
        print("----------------------------")

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
        
        if pos == 0:
            new_node.next = self.head.next
            self.head = new_node
            print("Node inserted sucessfully")
            return
        
        else:
            curr = self.head
            prev = None
            i= 0 
            while i < pos and curr != None:
                prev = curr
                curr = curr.next
                i += 1

            if i != pos:
                print("Invalid Position")
                return

            prev.next = new_node
            new_node.next = curr
            print("Node Inserted Succesfully")
            return

    # Deletion from the beginning
    def delete_from_beginning(self):

        # Check for empty list
        if self.head == None:
            print("Empty linked list")
            return
        
        else:
            self.head = self.head.next
            print("Node deletion sucessfully")
            return 
        
    def delete_from_end(self):

        # Check for empty list
        if self.head == None:
            print("Empty Linked List")
            return
        
        # List with one node
        if self.head.next == None:
            self.head = None
            print("Node Deleted sucessfully")
            return
        
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next

            temp.next = None
            print("Node deleted sucessfully")
            return
        
    def delete_from_middle(self,pos):

        ## Check for empty list 
        if self.head == None:
            print("Empty list")
            return
        
        ## Invalid Position
        if pos < 0:
            print("Invalid Position")
            return
        
        if pos == 0:
            ## Delete from beginning
            self.head = self.head.next
            print("Node deleted sucessfully")
            return

        temp = self.head
        count = 0

        while temp != None and count < pos -1:
            temp = temp.next
            count += 1

        ## Position out of range
        if temp == None or temp.next == None:
            print("Position out of range")
            return
            
        temp.next = temp.next.next
        print("Node deleted sucessfully")
        return
    

    def display_list(self):

        ## Check for empty list
        if self.head == None:
            print("Empty linked list")
            return
        
        # Traversal
        temp = self.head

        while temp != None:
            print(temp.data)
            temp = temp.next

        print("------------------")
            


ll = LinkedList()   
# Create LinkedList object

ll.insert_at_beginning(10)
ll.insert_at_beginning(5)
ll.insert_at_beginning(0)

ll.insert_at_end(25)
ll.insert_at_end(30)

ll.display_list()

ll.insert_at_middle(15, 3)
ll.insert_at_middle(20, 4)

ll.display_list()

ll.delete_from_beginning()

ll.display_list()

ll.delete_from_end()

ll.display_list()

ll.delete_from_end()

ll.delete_from_middle(3)
ll.delete_from_middle(0)
ll.delete_from_middle(2)

ll.display_list()