from json import load, dump

class JsonDatabase:
    data = {}

    def __init__(self, filename, encoding = 'utf-8'):
        self.filename = str(filename)
        self.encoding = str(encoding)
        with open(str(self.filename), 'r', encoding = self.encoding) as f: self.data = load(f)
    
    def __getitem__(self, item): return self.data[item]
    def __setitem__(self, item, value): self.data[item] = value
    def commit(self): 
        with open(str(self.filename), 'w', encoding = self.encoding) as f: dump(self.data, f, indent = '\t')
    
    def keys(self): return self.data.keys()
    def items(self): return self.data.items()
    def values(self): return self.data.values()