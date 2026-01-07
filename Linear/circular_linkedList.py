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

            while temp.next != None:
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
            self.head == None
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
                print(temp.data)
                temp = temp.next
                if temp == self.head:
                    print("List ends")
                    break
    

                
        

