from flask import Flask, render_template, request, redirect, url_for, flash
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

class HangmanGame:
    def __init__(self):
        self.word_list = ["python", "hangman", "programming", "computer", "keyboard", "interface"]
        self.word_to_guess = random.choice(self.word_list)
        self.guesses_left = 6
        self.guessed_letters = set()
        self.wrong_letters = set()

    def display_word(self):
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word_to_guess])

    def make_guess(self, guess):
        if guess.isalpha() and len(guess) == 1:
            if guess in self.guessed_letters:
                flash("You already guessed that letter.")
            else:
                self.guessed_letters.add(guess)
                if guess not in self.word_to_guess:
                    self.wrong_letters.add(guess)
                    self.guesses_left -= 1

                if self.guesses_left == 0:
                    self.game_over("You lose! The word was " + self.word_to_guess)
                elif set(self.word_to_guess) <= self.guessed_letters:
                    self.game_over("Congratulations! You guessed the word.")
                else:
                    flash(f"Guesses left: {self.guesses_left}")
        else:
            flash("Please enter a valid single letter.")

    def game_over(self, message):
        flash(message)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        guess = request.form['guess'].lower()
        hangman_game.make_guess(guess)

    return render_template('hangman.html', hangman_game=hangman_game)

if __name__ == '__main__':
    hangman_game = HangmanGame()
    app.run(debug=True)
