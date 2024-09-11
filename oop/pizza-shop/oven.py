class PizzaOven:
    def __init__(self, pieces, max_temp):
        self.pieces = pieces  # atributos
        self.max_temp = max_temp # atributos

    def check_pizza_size(self, pizza):
        if pizza.pieces > self.pieces:
            print("Not enough space. Pizza is bigger than oven")
            exit()

    def bake(self, pizza, temperature, time):
        temp_by_minute = temperature/time

        self.check_pizza_size(pizza)

        for minute in range(time):
            print(f"Minute: {minute}")
            pizza.heat(temp_by_minute)

        print("==========================")
        print(f"Pizza is Ready!: {pizza}")
        print("==========================")
