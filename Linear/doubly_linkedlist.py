class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class Doubly_linkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self,data):
        new_node = Node(data)
        # LinkedList empty
        if self.head == None:
            self.head = new_node
            print("Node Inserted")
            return
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            print("Node Inserted")
            return
            
    def insert_end(self,data):
        new_node = Node(data)
        ## Empty list 
        if (self.head==None):
            print("Empty Linked List")
            return
        else:
            temp = self.head
            if (temp.next == None):
                temp.next = new_node
                new_node.prev = temp
                print("Node Inserted")
                return
            else:
                while (temp.next.next != None):
                    temp = temp.next
                temp.next.next = new_node
                new_node.prev = temp.next
                print("Node Inserted")
                return

    def insert_at_position(self, value, position):
        if position == 0:
            self.insert_beginning(value)
            return

        new_node = Node(value)
        temp = self.head
        index = 0

        while temp is not None and index < position - 1:
            temp = temp.next
            index += 1

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node
               
    def delete_beginning(self):
        # Empty list
        if (self.head == None):
            print("Empty List")
            return
        else:
            if(self.head.next == None):
                self.head = None
            else:
                self.head.next.prev = None
                self.head = self.head.next
            print("Deleted Sucessfully")
            return
    def delete_end(self):
        # Empty list
        if(self.head == None):
            print("Empty list")
            return
        else:
            if(self.head.next == None):
                self.head = None
            else:
                temp = self.head
                while(temp.next.next != None):
                    temp = temp.next
                temp.next.prev = None
                temp.next = None
            print("Node Deleted")
            return
        

    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 0:
            self.delete_beginning()
            return

        temp = self.head
        index = 0

        while temp is not None and index < position:
            temp = temp.next
            index += 1

        if temp is None:
            print("Position out of range")
            return

        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next


    def display_list(self):
        # Empty linked list
        if self.head == None:
            print("Empty Linked List")
            return
        else:
            temp = self.head
            while temp != None:
                print(temp.data,"->",end=" ")
                temp = temp.next
            return



l1 = Doubly_linkedList()
print("List created")

l1.insert_beginning(10)
l1.insert_beginning(5)
l1.insert_end(20)
l1.insert_at_position(15, 2)
l1.display_list()
l1.delete_beginning()
l1.delete_end()
l1.delete_at_position(1)
print("After Deletions:")
l1.display_list()
