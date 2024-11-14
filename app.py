from flask import Flask, request, jsonify, render_template
import psycopg2
from psycopg2.extras import RealDictCursor
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = psycopg2.connect(
        dbname="Mylibrary",
        user="postgres",
        password="745125",
        host="localhost",
        port='5432'
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/books', methods=['GET'])
def get_books():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM books ORDER BY id')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(books)

@app.route('/api/books', methods=['POST'])
def add_book():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO books (title, author, year, genre) VALUES (%s, %s, %s, %s) RETURNING id',
        (data['title'], data['author'], data['year'], data['genre'])
    )
    book_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'id': book_id, 'message': 'Book added successfully'})

@app.route('/api/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'UPDATE books SET title = %s, author = %s, year = %s, genre = %s WHERE id = %s',
        (data['title'], data['author'], data['year'], data['genre'], id)
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Book updated successfully'})

@app.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM books WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Book deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)