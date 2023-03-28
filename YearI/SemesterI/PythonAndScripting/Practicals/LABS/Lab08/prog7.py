print(f"Lab 8 SHUBHANG GUPTA {d}")
class Bird:
    
    def intro(self):
        print("There are many types of birds.")
        
    def flight(self):
        print("Most of the birds can fly but some cannot.")
        
class sparrow(Bird):
    
    def flight(self):
        print("Sparrow can fly.")
        
class ostrich(Bird):
    
    def flight(self):
        print("Ostrich cannot fly.")
        
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

