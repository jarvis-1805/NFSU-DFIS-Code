print(f"Lab 8 SHUBHANG GUPTA {d}")
class Dog:
    
    attr1 = "mammal"
    
    def __init__(self, name):
        self.name = name
        
Rodger = Dog("Rodgerig")
Tommy = Dog("Tommyln")

print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

