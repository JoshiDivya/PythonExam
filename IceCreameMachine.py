class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        arr1= [[x,y] for x in self.ingredients for y in self.toppings]
        return arr1

machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops())

machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce","orange"])
print(machine.scoops())