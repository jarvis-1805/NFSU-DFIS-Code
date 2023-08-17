print(f"Lab 8 SHUBHANG GUPTA {d}")
class base:
    
    def __init__(self):
        self.a="MscDFIS"
        self.__c="MscDFIS"
        print(self.__c)
        
class derived(base):
    
    def __init__(self):
        print("Calling the private member of base class.")
        print(self.__c)
        
obj1 = base()

print(obj1.a)

