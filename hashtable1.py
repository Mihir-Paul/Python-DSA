class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [ None for i in range(self.max)]
    
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h % self.max 
    
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        self.arr[h]= val 
        
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h]=None 
        
t=HashTable()
print(t.get_hash('august'))
t['march 7']=90
t['aug 8']=79
t['dec 19']=68
print(t['jam'])
del t['march 7']
t['jan 17']=80
print(t.arr)        