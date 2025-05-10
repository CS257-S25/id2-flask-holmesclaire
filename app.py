'''this code creates a flask app for the time use data for get top activity by age'''
from flask import Flask, request
from ProductionCode.get_top_by_age import get_most_common_top_activity

app = Flask(__name__)

@app.route('/')
def homepage():
    '''this function displays the homepage and message for how to find the data
    return: message for homepage
    '''
    return "Hello, this is the homepage for the leisure time data. " \
    "To see the most common activitiy that people spend their time on for a certain age" \
    " add a '/' to this URL followed by the age you would like to look at " \
    "(age options: 18, 23, 40, 56, 57, 71, 80)."

@app.route('/<int:age>', strict_slashes=False)
def get_top_activity(age):
    '''this function and route displays the top activity based on the specified age
    return: top activity
    '''
    result = get_most_common_top_activity(age)
    return result

@app.errorhandler(404)
def page_not_found(e):
    '''this function and error handler gives the user a message when they encounter a 404 error
    '''
    base_url = request.host_url.rstrip('/')
    return f"{e}. Wrong format, do this instead: {base_url}/*insert age* for example {base_url}/23"

@app.errorhandler(500)
def python_bug(e):
    '''this function and error handler gives the user a message when they encounter a 500 error
    '''
    return f"{e} Invalid age, choose a valid age based on the small dataset: 18, 23, 40, 56, 57, 71, 80"

if __name__ == '__main__':
    app.run(port=8000)
