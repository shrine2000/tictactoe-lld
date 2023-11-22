class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def make_move(self):
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))
        return row, col