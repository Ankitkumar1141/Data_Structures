"""
Queue is a  linear order data structure that works on the FIFO(First In First Out) principle.It allows the insertion and deletion of values from two different end that is rear and front.
Insertion -- > rear
Deletion -- > front
"""

class Queue:

    def __init__(self,size):
        self.size = size 
        self.queue = [None]*self.size
        self.rear = -1
        self.front = -1

    def insert_value(self,value):   ## INSERT

        # Overflow Check
        if self.rear == len(self.queue) -1:
            print("Queue Overflow")
            return

        else:
            self.rear += 1
            self.queue[self.rear] = value
            print("Sucessfully inserted")
            if self.front == -1:
                self.front = 0
            return

    def delete_value(self):    ## DELETE

        ## Underflow Check
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow")
            return
        
        else:
            value = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            print("Deleted Sucessfully")
            return

    def display_queue(self):             ## DISPLAY
        for i in range(0,len(self.queue)):
            print(self.queue[i])

    def print_variable(self):
        print(f"Current rear value is {self.rear}")
        print(f"Current front value is {self.front}")


queue1 = Queue(8)
queue1.insert_value(5)
queue1.insert_value(10)
queue1.insert_value(15)
queue1.insert_value(20)

queue1.print_variable()

queue1.display_queue()

queue1.delete_value()
queue1.delete_value()

queue1.print_variable()
queue1.display_queue()



    
            