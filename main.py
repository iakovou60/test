class Hello:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
p1 = Hello("stavros")
print(p1.name)


