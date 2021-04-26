# pyhton program to implement a linked list ( singly Linked list )

# node class

class Node:

    # intializing the node 
    def __init__(self,data):
        self.data = data # assign the data to node 
        self.next = None # initialize as the next null


# Linked List Class

class LinkedList:

    # initialize the list 
    def __init__(self):
        self.head = None


    #print list 
    def print(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next


    # adding a new Node at beginning = O(1) 
    def push(self,newData):
        # allocate the node and put in new data
        newNode = Node(newData)

        # make next of newNode as head
        newNode.next = self.head

        # Move head pointer to newNode
        self.head = newNode


    # adding a new Node at middle = O(n) to access and O(1) to add
    def insertAfter(self,new,prev):
        # check if prev node exists
        if prev is None:
            print("N/A")
            return

        # make a new node and add data to it
        new = Node(new)

        # make the next of new node as the next of prev Node 
        #whatever will be the next elemnt of prev Node will be next elemnt of new Node
        new.next = prev.next

        # make the next of prev as the new Node
        prev.next = new


    # addn node to end of list
    def append(self, new):

        # create node
        # traverse the list starting at head
        # add the last.next = new node

        new = Node(new)

        if self.head is None:
            self.head = new
            return

        temp = self.head
        while (temp.next):
            temp = temp.next

        temp.next = new
        

        
        







if __name__ == '__main__':

    # start with empty list
    llist = LinkedList()

    llist.head = Node(3)
    second = Node(1)
    third = Node(7)

    # linking the list
    llist.head.next = second
    second.next = third


    # adding node to head
    llist.push(7)
    llist.push(8)


    #appending the node
    llist.append(15)
    llist.append(15)


    #print list
    llist.print()