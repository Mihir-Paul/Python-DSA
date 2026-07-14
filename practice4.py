class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [[] for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False

        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break

        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)

        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

        return None

    def __delitem__(self, key):
        h = self.get_hash(key)

        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
                break

t = HashTable()

t["orange"] = 74
t["apple"] = 98
t["mango"] = 87
t["banana"] = 98

print("Orange :", t["orange"])
print("Apple  :", t["apple"])
print("Mango  :", t["mango"])
print("Banana :", t["banana"])

print("\nHash of grapes =", t.get_hash("grapes"))

print("\nComplete Hash Table:")
for bucket in t.arr:
    if bucket:
        print(bucket)

del t["apple"]

print("\nAfter deleting apple:")
for bucket in t.arr:
    if bucket:
        print(bucket)