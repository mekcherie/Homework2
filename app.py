from flask import Flask, request, render_template
import random

app = Flask(__name__)


def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')


@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/>
        What is youre favorite toppings?
        <input type="text" name="toppings">
        <input type="submit" value="Submit!">
    </form>
    """
    return render_template("froyo_form.html")

@app.route('/froyo_results')
def show_froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    users_froyo_toppings = request.args.get('toppings')
    return f'You ordered {users_froyo_flavor} with {users_froyo_toppings} Fro-Yo!'

    context = {
        "users_froyo_flavor" : request.args.get('flavor'),
        "users_froyo_topping" : request.args.get('toppings')
    }
    return render_template("froyo_results.html", **context)

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite color? <br/>
        <input type="text" name="color"><br/>
        What is your favorite animal? <br/>                            
        <input type="text" name="animal"><br/>
        What is your favorite city? <br/>
        <input type="text" name="city""><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    users_fav_color = request.args.get('color')
    users_fav_animal = request.args.get('animal')
    users_fav_city = request.args.get('city')
    return f'Wow, it/s amazing that {users_fav_color} {users_fav_animal} lives in {users_fav_city}!'

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
    Any thing that you need to make it a secret<br/>
    <input type="text" name="message">
    <br/>  <br/>
    <input type="submit" value="Submit">
    </form>
    """


@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    users_secret_message = request.form.get('message')
    secret_message = sort_letters(users_secret_message)

    return f"this is your {secret_message}!"


@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return """
    <form action = "/calculator_results" method = "GET" >
        Please enter 2 numbers and select an operator. <br/> <br/>
        <input type = "number" name = "operand1" >
        <select name = "operation" >
            <option value = "add"> + </option>
            <option value = "subtract"> - </option>
            <option value = "multiply"> * </option>
            <option value = "divide"> / </option>
        </select >
        <input type = "number" name = "operand2">
        <input type = "submit" value = "Submit!">
    </form >
    """
    return render_template("calculator_form.html")

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    user_operand1 = request.args.get("operand1")
    user_operand2 = request.args.get("operand2")
    user_operation = request.args.get("operation")
    
    if user_operation == "add":
        result = int(user_operand1) + int(user_operand2)
        chosen_operation = "add"
    elif user_operation == "subtract":
        result = int(user_operand1) - int(user_operand2)
        chosen_operation = "subtract"
    elif user_operation == "multiply":
        result = int(user_operand1) * int(user_operand2)
        chosen_operation = "multiply"
    elif user_operation == "divide":
        result = int(user_operand1) / int(user_operand2)
        chosen_operation = "divide"
    
    context = {
        "num1" : user_operand1,
        "num2" : user_operand2,
        "result" : result,
        "operation" : chosen_operation
    }
    return render_template("calculator_results.html", **context)


# List of compliments to be used in the `compliments_results` route (feel free
# to add your own!)
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]


@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    pass
    # return render_template('compliments_form.html')


@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    pass

    # return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run()
