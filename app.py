from flask import Flask, render_template, request, flash, redirect, url_for, Response, abort
import random, time


app = Flask(__name__)


class NationalBingo(object):
    win_list = []
    player_nums = []
    win_choice = []
    player_select = []
    bonus_win = 0
    player_bonus = 0
    matching_numbers = []
    player_html_elements = []
    win_html_elements = []
    match_html_elements = []

    node_map = {
        'grey':     [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'blue':     [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        'pink':     [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
        'green':    [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
        'yellow':   [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    }

    html_nodes = {
        'grey': '<span class="dot grey"><span class="inner-dot"><h2>{}</h2></span></span>',
        'blue': '<span class="dot blue"><span class="inner-dot"><h2>{}</h2></span></span>',
        'pink': '<span class="dot pink"><span class="inner-dot"><h2>{}</h2></span></span>',
        'green': '<span class="dot green"><span class="inner-dot"><h2>{}</h2></span></span>',
        'yellow': '<span class="dot yellow"><span class="inner-dot"><h2>{}</h2></span></span>'
    }

    def __doc__(self):
        return '''
                Initialisation:
                    -First we need to reset the last game. We do this by setting the variables to
                     their respective empty default data types.
                    -Next we create two lists of numbers 1-49
                    -After that we take a "random.sample" of both of these lists created in previous step.
                     We then have 1. A list of the winning numbers and 2. A list of numbers selected
                     randomly on behalf of the player. These numbers CANNOT appear twice in any list, ever.
                    -We also select the bonus numbers. The winning bonus number and they players bonus number.
                     Utilises a similar function, however this may duplicate the numbers **psuedo** framework
                     for bonus ball, which is not yet implemented in the game.
                    -Next we enumerate the list of numbers selected for the player, this built-in returns two values,
                     the index and the value of that index. We check of the number (v) is present in the winning
                     numbers list and append v to the matching numbers list.
                    -I created a function that writes the relevant HTML elements based on the numbers and colors.
                
                Functions:
                    -print_out()
                        Used in the early stages to verify numbers and uniqueness of numbers etc.
                    
                    -html_output()
                        Iterates through lists and matches numbers to colors and then colors to html templates
                        
                    -home()
                        This is a flask route. On the website it's the welcome page.
                        
                    -play()
                        This is a flask route. On the website, it's the page where you play a game.
                '''

    def __init__(self):
        self.win_choice = []
        self.player_select = []
        self.bonus_win = 0
        self.player_bonus = 0
        self.matching_numbers = []
        self.html_elements = []
        self.player_html_elements = []
        self.win_html_elements = []
        self.match_html_elements = []

        self.win_list = [x+1 for x in range(49)]
        self.player_nums = [x+1 for x in range(49)]
        self.win_choice = random.sample(self.win_list, 6)
        self.player_select = random.sample(self.player_nums, 6)
        self.bonus_win = random.choice(self.win_list)
        self.player_bonus = random.choice(self.win_list)

        for i, v in enumerate(self.player_select):
            if v in self.win_choice:
                self.matching_numbers.append(v)

        self.html_output()

    def print_out(self):
        print(sorted(self.win_choice))
        print(sorted(self.player_select))
        print(self.bonus_win)
        print(self.player_bonus)
        print(sorted(self.matching_numbers))

    def html_output(self):
        for x in sorted(self.player_select):
            for y, z in self.node_map.items():
                if x in z:
                    self.player_html_elements.append(self.html_nodes[y].format(str(x)))
        for x in sorted(self.win_choice):
            for y, z in self.node_map.items():
                if x in z:
                    self.win_html_elements.append(self.html_nodes[y].format(str(x)))
        for x in sorted(self.matching_numbers):
            for y, z in self.node_map.items():
                if x in z:
                    self.match_html_elements.append(self.html_nodes[y].format(str(x)))


@app.route('/')
def home():
    return render_template('home.html', nb=NationalBingo())


@app.route('/play')
def play():
    return render_template('play.html', nb=NationalBingo())


@app.route('/code')
def code():
    return render_template('code.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
