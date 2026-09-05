from flask import Flask, request, render_template

import requests #a further import is included here for redirection (this is used to automate the testing of the POST request), the form option, however, is the correct approach

app = Flask(__name__)



@app.route('/')
def default():
    return render_template("../pages/form.html")
    

if __name__ == '__main__':
    app.run(debug=True)
