class ListDictionary:
    def __init__(self):
        # implement the constructor
        self.dictionary = []

    def insert(self, key, value):
        # implement the insert() method
        if key in self.dictionary:
            index = self.dictionary.index(key)
            if self.dictionary[index + 1] == [value]:
                return True
            else:
                self.dictionary[index + 1].insert(0, value)
                self.dictionary[index + 1].pop(1)
        else:
            self.dictionary.append(key)
            self.dictionary.append([value])

    # implement the rest of the dictionary methods below

