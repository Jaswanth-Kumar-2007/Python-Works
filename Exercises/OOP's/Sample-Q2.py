class Material: 
    def __init__(self, elements): 
        self.elements = elements 
    def process(self): 
        return [e.upper() for e in self.elements] 
class Alloy(Material): 
    def process(self): 
        return sorted(set(super().process() + ['ZINC'])) 
a = Alloy(['iron', 'carbon', 'iron'])
print(a.process()) 