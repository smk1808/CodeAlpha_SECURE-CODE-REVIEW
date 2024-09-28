from flask import Flask, request, render_template_string
import sqlite3
from werkzeug.security import generate_password_hash

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Simple input validation
        if len(username) < 3 or len(password) < 8:
            return 'Invalid username or password'

        hashed_password = generate_password_hash(password)
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        conn.close()

        return 'User registered successfully!'

    return render_template_string('''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Register">
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=False)



