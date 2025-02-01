"""  insertion  node in the linked list"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linkedlist:
    def __init__(self):
        self.head=None
        self.counter=0
        
    # insetion the new node at the beginning of the linked list
    def insertionAtBeigining(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
        self.counter+=1
    def printLinked_list(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
    def insertionAtending(self,newdata):
        # first check the wether is already node or not in the {self.head}
        
        if self.head is None:
            self.insertionAtBeigining(newdata)
        else:
            temp=self.head
            while temp.next is not None:
                # jsut go for the last node
                temp=temp.next
        self.counter+=1
    """it jsut reversing the single linked list"""
    def reverseTheSingleLinkedList(self):
        prev=None
        next=None
        curr=self.head
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
    def lengthOf(self):
        print(self.counter)
        
    def insertionAtBetween(self,val,newNode):
        if self.head is  None:
            return f"Sorry your linked list is none we can't inset at {newNode}"
        temp=self.head
        while temp:
            if temp.data==val:
                endnode=temp.next
                newnodeOne=Node(newNode)
                temp.next=newnodeOne
                newnodeOne.next=endnode
                self.counter+=1
                return "it is sucsesss"
            else:
                temp=temp.next
        return f"Sorry for in convinece of this val-----> {val} is not presetn in the linkedList please     give some other value presented in the linked list"
    def deleteTheNodeinLinkedLIst(self,position):
        if self.head is None:
            return 'linked list is empty'
        temp=self.head
        for i in range(position-1):
            # print(temp.data)
            temp=temp.next
            if temp.next is None:
                return "sorry there is no such range index"

        
        point=temp.next
        temp.next=point.next
        self.counter-=1
    """ Searching  the node """
    def searchNode(self,node):
        temp=self.head
        while temp:
            if temp.data==node:
                return True
            temp=temp.next
        return False
        
            
header=Linkedlist()
for i in range(5,-1,-1):
    header.insertionAtBeigining(i)
# header.insertionAtending(45)
# header.insertionAtBetween(99,89)
# header.printLinked_list()
# header.reverseTheSingleLinkedList()
# header.deleteTheNodeinLinkedLIst(2)
# header.deleteTheNodeinLinkedLIst(2)
header.lengthOf()
header.printLinked_list()
print(header.searchNode(3))

        