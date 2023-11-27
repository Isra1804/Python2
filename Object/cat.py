class cat:
    def __init__(self, name, age, color, type, stepsPerWalk, stepsPerRun):
        self.name = name
        self.age = age
        self.color = color
        self.type = type
        self.stepsPerWalk = stepsPerWalk
        self.stepsPerRun = stepsPerRun
    
    def properties(self):
        print(f"I am {self.name}, I am {self.age} monthes old, My color is {self.color}, I am a {self.type} cat.")

    def methods(self):
        print(f"I walk {self.stepsPerWalk} steps/sec, and {self.stepsPerWalk} runs/sec.")

        
    
