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


    # adding a new Node at beginning
    def push(self,newData):
        # allocate the node and put in new data
        newNode = Node(newData)

        # make next of newNode as head
        newNode.next = self.head

        # Move head pointer to newNode
        self.head = newNode

        
        







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


    #print list
    llist.print()