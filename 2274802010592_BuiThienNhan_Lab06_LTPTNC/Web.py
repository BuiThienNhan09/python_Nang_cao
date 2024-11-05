# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cần thiết cho session và flash messages

# Thông tin đăng nhập mẫu (trong thực tế nên sử dụng database)
USERS = {
    'admin': 'password123'
}

# Decorator để kiểm tra đăng nhập
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Vui lòng đăng nhập để tiếp tục')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in USERS and USERS[username] == password:
            session['username'] = username
            flash('Đăng nhập thành công!')
            return redirect(url_for('calculator'))
        else:
            flash('Tên đăng nhập hoặc mật khẩu không đúng')
    
    return render_template('login.html')

@app.route('/calculator', methods=['GET', 'POST'])
@login_required
def calculator():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']
            
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 == 0:
                    flash('Không thể chia cho 0!')
                else:
                    result = num1 / num2
        except ValueError:
            flash('Vui lòng nhập số hợp lệ')
    
    return render_template('calculator.html', result=result)

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Đã đăng xuất thành công')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
