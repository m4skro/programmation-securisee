# Import the necessary modules from Flask library
from flask import Flask, request, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the index page
@app.route('/')
def index():
    # Render the form template
    return render_template('form.html')

# Define a route for submitting the form
@app.route('/submit', methods=['POST'])
def submit():
    # Get the user's feedback from the form
    avis = request.form['avis']

     # Render the template that displays the feedback
    return render_template('avis.html', avis=avis)

# Run the application if this file is executed as the main program
if __name__ == '__main__':
    app.run()
