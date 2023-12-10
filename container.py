
from Marble import Marble
from Point import Point
import turtle as t

# Define the leaderboard file path
leaderboard_file = "leaderboard.txt"

class Container:
    def __init__(self, x, y, width, height, border_thickness=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_thickness = border_thickness
        self.pen = t.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)  # Draw at the fastest speed

    def draw(self):
        self.pen.pensize(self.border_thickness)  # Set the border thickness
        self.pen.penup()
        self.pen.goto(self.x, self.y)
        self.pen.pendown()
        for _ in range(2):
            self.pen.forward(self.width)
            self.pen.right(90)
            self.pen.forward(self.height)
            self.pen.right(90)
        self.pen.penup()

class GameDisplay(Container):
    def __init__(self):
        super().__init__(x=-280, y=360, width=350, height=540, border_thickness=4)
        self.guess_marbles = []
        self.indicator_marbles = []

    def draw_marbles_and_indicators(self):
        yOffset = 100
        for row in range(10):  # 10 rows
            row_guess_marbles = []
            row_indicator_marbles = []
            for col in range(4):  # 4 guesses per row
                guess_position = Point(-250 + col * 50, 210 - row * 50 + yOffset)
                guess_marble = Marble(guess_position, "grey", 15)
                row_guess_marbles.append(guess_marble)
                guess_marble.draw_empty()

            for i in range(2):  # Two columns of indicators
                for j in range(2):  # Two rows of indicators
                    indicator_position = Point(-120 + i * 20, 210 - row * 50 + yOffset + j * 20)
                    indicator_marble = Marble(indicator_position, "white", 5)
                    row_indicator_marbles.append(indicator_marble)
                    indicator_marble.draw_empty()

            self.guess_marbles.append(row_guess_marbles)
            self.indicator_marbles.append(row_indicator_marbles)

class Leaderboard(Container):
    def __init__(self):
        super().__init__(x=100, y=360, width=150, height=540, border_thickness=4)

    def draw_leaderboard(self):
        self.draw()
        leaderboard_data = self.read_leaderboard()
        self.display_leaderboard(leaderboard_data)

    def read_leaderboard(self):
        try:
            with open(leaderboard_file, "r") as file:
                lines = file.readlines()
            leaderboard = [line.strip().split(",") for line in lines]
            leaderboard.sort(key=lambda x: int(x[1]))
            return leaderboard
        except FileNotFoundError:
            return []

    def display_leaderboard(self, leaderboard_data):
        leaderboard_pen = t.Turtle()
        leaderboard_pen.hideturtle()
        leaderboard_pen.penup()
        leaderboard_pen.goto(self.x + 10, self.y - 30)

        for i, (name, score) in enumerate(leaderboard_data[:5]):
            leaderboard_pen.write(f"{i + 1}. {name} - {score}", align="left", font=("Arial", 12, "normal"))
            leaderboard_pen.goto(self.x + 10, self.y - 30 - (i + 1) * 20)

class UserBoard(Container):
    def __init__(self):
        super().__init__(x=-280, y=-180, width=350, height=200, border_thickness=4)

def main():
    t.bgcolor("white")
    t.title("Mastermind Game")
    game_display = GameDisplay()
    leaderboard = Leaderboard()
    userboard = UserBoard()
    game_display.draw()
    leaderboard.draw_leaderboard()
    userboard.draw()
    game_display.draw_marbles_and_indicators()
    t.done()

if __name__ == "__main__":
    main()
