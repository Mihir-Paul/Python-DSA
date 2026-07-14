class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [ None for i in range(self.max)]
        
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h % self.max 
    
    def __setitem__(self, key,val):
        h= self.get_hash(key)
        self.arr[h]= val
        
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h] 
    
    def __delitem__(self, key):
        h= self.get_hash(key)
        self.arr[h]=None
        
t=HashTable()
print(t.get_hash('lemon'))
t['sync']=90
t['apple']=30
t['sham4']= 50
del t['sham4']
print(t['banana'])
print(t.arr)