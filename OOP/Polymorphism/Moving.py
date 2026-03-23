class Bird:
    def move(self):
        return "Flying in the sky"

class Fish:
    def move(self):
        return "Swimming in the water"

bird = Bird()
fish = Fish()
types_of_moves = [bird.move, fish.move]
for move in types_of_moves:
    print(move())

