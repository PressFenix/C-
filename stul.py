class Chair:
    def __init__(self, Стул, material, color):
        self.Стул = Стул
        self.material = material
        self.color = color

    def __str__(self):
        return (f"Стул:({self.Стул}, {self.material}, {self.color})")
    def __repr__(self):
        return (f"Стул:({self.Стул}, {self.material}, {self.color})")

standart = Chair("Kostya", "wood", "black")

print([standart])


