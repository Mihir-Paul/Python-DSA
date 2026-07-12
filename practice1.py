class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next 
class LinkedList():
    def __init__(self):
        self.head = None 
    
    def _insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
        
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            
        itr = self.head 
        llstr=''
        while itr:
            llstr+=str(itr.data)+"<--"
            itr=itr.next 
        print(llstr)
        
    def _insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
         
        itr=self.head 
        while itr.next:
            itr= itr.next 
        itr.next = Node(data,None)
        
    def insert_values(self,data_values):
        self.head = None 
        for data in data_values:
            self._insert_at_end(data)
            
    def get_length(self):
        count=0
        itr=self.head 
        while itr:
            itr=itr.next 
            count+=1 
        return count 
    
    def remove_at(self,index):
        if index<0 and index>=self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next 
            return 
        
        itr=self.head  
        count=0
        while itr:
            if count == index-1:
                itr.next = itr.next.next 
                break 
            itr = itr.next 
            count+=1 
        
    def insert_at(self,index,data):
        if index<0 and index>=self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self._insert_at_beginning(data)
            return 
        
        itr=self.head  
        count=0
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break 
            itr = itr.next 
            count+=1 

ll=LinkedList()
ll._insert_at_beginning(7)
ll._insert_at_beginning(5)
ll._insert_at_end(9)
ll.print()
ll.insert_values([8,56,78,89])
ll.print()
print("Length:", ll.get_length())
ll.remove_at(2)
ll.print()
ll.insert_at(1,96)
ll.print()
           