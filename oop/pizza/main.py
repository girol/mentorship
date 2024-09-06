from classes import Pizza

# instance of a class here:
# mozzarela is an object from the class Pizza
mozzarella = Pizza(border="normal", pieces=6, filing="mozzarella")

# We are calling the method order() declared inside the class
mozzarella.order()

chicken = Pizza(border="cream cheese", pieces=8, filing="chicken")
chicken.order()

mushroom = Pizza(border="no", pieces=20, filing="mushrooms")
mushroom.order()
