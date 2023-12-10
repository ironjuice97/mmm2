
import turtle as t
from Marble import Marble
from Point import Point
from random import shuffle
from os import path
from container import GameDisplay, Leaderboard, UserBoard

class MastermindGame:
    def __init__(self):
        self.leaderboard_file = "leaderboard.txt"
        self.current_row = 0
        self.current_col = 0
        self.gameover = False
        self.ans_count = 1
        self.ans_limit = 10
        self.colors = ["blue", "red", "green", "yellow", "purple", "black"]
        self.display_colors = self.colors.copy()
        self.available_colors_per_row = [self.colors.copy() for _ in range(10)]
        self.shuffled_colors = self.colors.copy()
        shuffle(self.shuffled_colors)
        self.code = self.shuffled_colors[:4]
        self.guess_marbles = [[Marble(Point(-250 + col * 50, 210 - row * 50), "grey", 15) for col in range(4)] for row in range(10)]
        self.current_guess = []

    def get_player_name(self):
        return t.textinput("Player Name", "Enter your name:")

    def setup_color_picker(self):
        color_picker_turtle = t.Turtle()
        color_picker_turtle.penup()
        color_picker_turtle.hideturtle()
        color_picker_turtle.speed('fastest')

        start_x = -110
        start_y = -250
        for index, color in enumerate(self.colors):
            t.register_shape(color + "_circle", ((-10, -10), (-10, 10), (10, 10), (10, -10)))
            button = t.Turtle(shape=color + "_circle")
            button.color(color)
            button.penup()
            button.goto(start_x + index * 50, start_y)
            button.onclick(lambda x, y, color=color: self.on_color_selected(color))

    def setup_game_screen(self):
        game_display = GameDisplay()
        leaderboard = Leaderboard()
        userboard = UserBoard()
        game_display.draw()
        leaderboard.draw_leaderboard()
        userboard.draw()
        for row in self.guess_marbles:
            for marble in row:
                marble.draw_empty()

    def on_color_selected(self, color):
        if len(self.current_guess) < 4 and color not in self.current_guess:
            self.current_guess.append(color)
            self.update_game_board()

    def update_game_board(self):
        for i, color in enumerate(self.current_guess):
            self.guess_marbles[self.current_row][i].set_color(color)
            self.guess_marbles[self.current_row][i].draw()

    def main(self):
        player_name = self.get_player_name()
        wn = t.Screen()
        wn.title("Mastermind")
        wn.bgcolor("white")
        wn.setup(width=600, height=800)

        self.setup_game_screen()
        self.setup_color_picker()

        if not path.exists(self.leaderboard_file):
            open(self.leaderboard_file, "x").close()

        t.listen()
        t.mainloop()

if __name__ == "__main__":
    game = MastermindGame()
    game.main()
