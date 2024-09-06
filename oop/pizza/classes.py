class Pizza:
    def __init__(self, filing, border, pieces=4):
        self.filling = filing
        self.border = border

        if pieces not in [4, 6, 8]:
            print("Pieces available: 4, 6, 8")
            exit()

        self.pieces = pieces

    def order(self):
        print(
            f"""
        Order:
        Border: {self.border}
        Filling: {self.filling}
        Pieces: {self.pieces}

        """
        )
