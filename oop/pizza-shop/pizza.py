class Pizza:
    current_temperature = 35

    def __init__(self, filing, border, pieces=4, bake_temperature=180, cooking_time=15):
        self.filling = filing
        self.border = border
        self.bake_temperature = bake_temperature
        self.cooking_time = cooking_time

        if pieces not in [4, 6, 8]:
            print("Pieces available: 4, 6, 8")
            exit()

        self.pieces = pieces

    def __str__(self):
        return self.filling

    def order(self):
        print(
            f"""
                Order:
                Border: {self.border}
                Filling: {self.filling}
                Pieces: {self.pieces}
                Cooking Time: {self.cooking_time}
                Temperature: {self.temperature}
        """
        )

    def heat(self, temperature_to_raise):
        self.current_temperature += temperature_to_raise
