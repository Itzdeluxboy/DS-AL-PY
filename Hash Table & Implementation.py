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
print(len(data_list) == 4096)
#QUESTION 2: Complete the get_index function below which implements the hashing algorithm described above.
def get_index(data_list, a_string):
    result = 0
    
    for a_character in a_string:
        a_number= ord(a_character)

        result += a_number

    list_index = result%len(data_list)
    return list_index

print(get_index(data_list, 'Aakash'))
