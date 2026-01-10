## Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class circular_linkedlist:

    def __init__(self):
        self.head = None

    def insert_beginning(self,data):
        new_node = Node(data)
        ## Empty list
        if self.head == None:
            self.head = new_node
            new_node.next = new_node
            print("Inserted Sucessfully")
            return
        
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            new_node.next = self.head
            temp.next = new_node
            self.head = new_node
            print("Inserted sucessfully")
            return
        
    def insert_end(self,data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            new_node.next = new_node
            print("Inserted sucessfully")
            return
        
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head
            print("Inserted sucessfully")
            return
        
    def insert_position(self, data, pos):
        new_node = Node(data)

        # Case 1: Empty list
        if self.head is None:
            if pos == 0:
                self.head = new_node
                new_node.next = new_node
                print("Node inserted successfully")
            else:
                print("Invalid position")
            return

        # Case 2: Insert at beginning (pos = 0)
        if pos == 0:
            temp = self.head

            # Find last node
            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head
            self.head = new_node
            print("Node inserted successfully")
            return

        # Case 3: Insert at middle or end
        curr = self.head
        index = 0

        while curr.next != self.head and index < pos - 1:
            curr = curr.next
            index += 1

        if index != pos - 1:
            print("Invalid position")
            return

        new_node.next = curr.next
        curr.next = new_node
        print("Node inserted successfully")

        
    def delete_beginning(self):

        if self.head == None:
            print("Empty list")
            return
        
        elif self.head.next == self.head:
            self.head = None
            print("Deleted sucessfully")
            return
        
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
            print("Deleted sucessfully")
            return
        
    def delete_end(self):
        if self.head == None: ## Empty list
            print("Empty list")
            return
        elif self.head.next == self.head:  ## Single node list
            self.head = None
            print("Deleted sucessfully")
            return
        
        else:
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next

            temp.next = self.head


            
        
    def display_linkedlist(self):

        if self.head == None:
            print("Empty linked list")
            return
        
        else:
            temp = self.head
            while True:
                print(f"{temp.data}")
                temp = temp.next
                if temp == self.head:
                    print("List ends")
                    break
    



l1 = circular_linkedlist()  
l1.insert_beginning(30)
l1.insert_beginning(20)
l1.insert_beginning(10)
l1.insert_end(40)
l1.insert_end(70)
l1.insert_position(50,4)
l1.insert_position(60,5)

print("------------------------------------------------------------")
l1.display_linkedlist()
l1.delete_beginning()
l1.delete_end()

l1.display_linkedlist()