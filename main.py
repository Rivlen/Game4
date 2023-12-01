from flask import Flask, request, render_template

app = Flask(__name__, template_folder="templates")


@app.route('/', methods=['GET', 'POST'])
def main_page():
    global min_number, max_number, guess
    if request.method == "GET":
        min_number = 0
        max_number = 1000
        guess = int((max_number - min_number) / 2) + min_number
        return render_template("main_page.html", guess=guess)

    elif request.method == "POST":
        result = request.form.get('result')
        if result == "You win":
            guess = "that I'm the best!"
        elif result == "Too big":
            max_number = guess
            guess = int((max_number - min_number) / 2) + min_number
        elif result == "Too small":
            min_number = guess
            guess = int((max_number - min_number) / 2) + min_number
        return render_template("main_page.html", guess=guess)


if __name__ == '__main__':
    min_number = 0
    max_number = 1000
    guess = int((max_number - min_number) / 2) + min_number
    app.run(debug=True)
