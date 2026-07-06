from flask import Flask, request

app = Flask(__name__)

correct_username = "admin"
correct_password = "hunter2"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == correct_username and password == correct_password:
            return "Welcome!"
        else:
            return "Invalid credentials!"
    return '''
    <form method="POST">
        Username: <input type="text" name="username" /><br/>
        Password: <input type="password" name="password" /><br/>
        <input type="submit" value="Login" />
    </form>
    '''

if __name__ == '__main__':
    app.run(port=34224)