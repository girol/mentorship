from pizza import Pizza
from oven import PizzaOven

# # prepare:
mozzarella = Pizza(border="normal", pieces=6, filing="mozzarella")
peperoni = Pizza(border="normal", pieces=4, filing="peperoni")


medium_oven = PizzaOven(pieces=6, max_temp=180)
small_oven = PizzaOven(pieces=4, max_temp=180)

temperature = 180
time = 15

medium_oven.bake(mozzarella, temperature, time)
small_oven.bake(peperoni, temperature, time)
