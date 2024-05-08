from flask import Flask, render_template, request

app = Flask(__name__, template_folder='../website')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        city = request.form['city']
        age = int(request.form['age'])
        dob = request.form['dob']

        message = "Try again when you are 18"
        if age > 18:
            message = "Welcome to our site!"

        # Validate City input
        if not city.isalpha():
            message = "Enter a valid city"

        welcome_message = f"Hello {first_name} {last_name}, I see that your date of birth is {dob}"

        return render_template('registration/result.html', welcome_message=welcome_message, message=message)

    return render_template('registration/index.html')

@app.route('/store', methods=['GET', 'POST'])
def store():
    return render_template('store/index.html')


if __name__ == '__main__':
    app.run(debug=True)
