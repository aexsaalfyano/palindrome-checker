from flask import Flask, render_template, request

app = Flask(__name__)

def is_palindrome(string):
    string = string.lower().replace(' ', '')
    return string == string[::-1]

@app.route('/', methods=['GET', 'POST'])
def index():
    palindrome_result = None
    if request.method == 'POST':
        input_text = request.form['input_text']
        palindrome_result = is_palindrome(input_text)
    return render_template('index.html', palindrome_result=palindrome_result)

if __name__ == '__main__':
    app.run(debug=True)
