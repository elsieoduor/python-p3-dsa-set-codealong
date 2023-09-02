class MySet:
    def __init__(self, enumerable =[]):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary.put(value) = True
    
    def has(value):
        return value in self.dictionary
    
    def __str__(self):
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'

    def add(self, value):
        self.dictionary[value] = True
        return self
    def delete(self, value):
        self.dictionary.pop(value, None)
    
    def size(self):
        len(self.dictionary)
        
    def clear(self):
        self.dictionary.clear()