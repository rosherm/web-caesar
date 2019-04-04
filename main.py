from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                    background-color: #eee;
                }
            </style>
        </head>
        <body>
        <form action = "/" method = "post">
        <label>
            Rotate by:        
            <input type = "text" name = "rot" value = "0">
            <br>
            <input type = "textarea" name = "text">
            <br>
            <input type = "submit" value = "Submit Query">
        </label>  
        </form>
        </body>
    </html>
    """

@app.route("/", methods =['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']

    rot_int = int(rot)
    text = str(text)

    text_rot = rotate_string(text, rot)

    return "<h1>" + text_rot + "</h1>"
    
@app.route("/")
def index():
    return form

app.run()