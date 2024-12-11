class HashTable:
    def insert(self,key,value):
        pass
    def find(self,key):
        pass
    def update(self, key, value):
        pass
    def list_all(self):
        pass

#QUESTION 1: Create a Python list of size `MAX_HASH_TABLE_SIZE`, with all the values set to `None`.
data_list = [None] * 4096

#QUESTION 2: Complete the get_index function below which implements the hashing algorithm described above.
def get_index(data_list, a_string):
    result = 0
    
    for a_character in a_string:
        a_number= ord(a_character)

        result += a_number

    list_index = result%len(data_list)
    return list_index



#QUESTION 3: Complete the hash table implementation
MAX_HASH_TABLE_SIZE = 4096

class BasicHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None]*max_size

    def insert(self,key,value):
        idx = get_index(self.data_list, key)
        self.data_list[idx] = (key, value)

    def find(self,key):
        idx = get_index(self.data_list,key)
        kv = self.data_list[idx]

        if kv is None:
            return None
        else:
            key, value = kv
            return value
        
    def update(self, key, value):
        idx=get_index(self.data_list, key)
        self.data_list[idx] = (key,value)

    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]
        
basic_table = BasicHashTable(max_size=4096)

print(len(basic_table.data_list) == 4096)

basic_table.insert('Aakash', '9999999999')
basic_table.insert('Hemanth', '8888888888')
print(basic_table.find('Hemanth') == '8888888888')