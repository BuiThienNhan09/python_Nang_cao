import psycopg2
import tkinter as tk
from tkinter import ttk, messagebox

def connect_db(dbname='postgres'):
    try:
        conn = psycopg2.connect(
            dbname="Mylibrary", 
            user="postgres", 
            password="745125", 
            host="localhost", 
            port='5432'
        )
        return conn
    except Exception as e:
        print(f"Error while connecting to database {dbname}:", e)
        raise

def create_table(connection):
    if connection is None:
        messagebox.showerror("Database Error", "Unable to connect to the database")
        return
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author VARCHAR(255) NOT NULL,
                year INTEGER NOT NULL,
                genre VARCHAR(100) NOT NULL
            );
        """)
        connection.commit()
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        if cursor:
            cursor.close()

def add_book():
    title = entry_title.get()
    author = entry_author.get()
    year = entry_year.get()
    genre = entry_genre.get()
    
    if not all([title, author, year, genre]):
        messagebox.showwarning("Lỗi", "Vui lòng điền đầy đủ thông tin")
        return
        
    try:
        int(year)
    except ValueError:
        messagebox.showwarning("Lỗi", "Năm xuất bản phải là số")
        return
        
    try:
        conn = connect_db('books')
        cur = conn.cursor()
        cur.execute("INSERT INTO books (title, author, year, genre) VALUES (%s, %s, %s, %s)",
                    (title, author, int(year), genre))
        conn.commit()
        cur.close()
        conn.close()
        reload_books()
        clear_entries()
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

def update_book():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Lỗi", "Vui lòng chọn sách cần cập nhật")
        return
        
    book_id = tree.item(selected[0])['values'][0]
    title = entry_title.get()
    author = entry_author.get()
    year = entry_year.get()
    genre = entry_genre.get()
    
    if not all([title, author, year, genre]):
        messagebox.showwarning("Lỗi", "Vui lòng điền đầy đủ thông tin")
        return
        
    try:
        conn = connect_db('books')
        cur = conn.cursor()
        cur.execute("UPDATE books SET title=%s, author=%s, year=%s, genre=%s WHERE id=%s",
                    (title, author, int(year), genre, book_id))
        conn.commit()
        cur.close()
        conn.close()
        reload_books()
        clear_entries()
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

def delete_book():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Lỗi", "Vui lòng chọn sách cần xóa")
        return
        
    if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa sách này?"):
        book_id = tree.item(selected[0])['values'][0]
        try:
            conn = connect_db('books')
            cur = conn.cursor()
            cur.execute("DELETE FROM books WHERE id=%s", (book_id,))
            conn.commit()
            cur.close()
            conn.close()
            reload_books()
            clear_entries()
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

def reload_books():
    for item in tree.get_children():
        tree.delete(item)
    try:
        conn = connect_db('books')
        cur = conn.cursor()
        cur.execute("SELECT * FROM books")
        for row in cur.fetchall():
            tree.insert("", "end", values=row)
        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

def clear_entries():
    entry_title.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_year.delete(0, tk.END)
    entry_genre.delete(0, tk.END)

def on_tree_select(event):
    selected = tree.selection()
    if selected:
        item = tree.item(selected[0])['values']
        clear_entries()
        entry_title.insert(0, item[1])
        entry_author.insert(0, item[2])
        entry_year.insert(0, item[3])
        entry_genre.insert(0, item[4])

# Main window setup
root = tk.Tk()
root.title("Quản lý thư viện")
root.geometry("700x500")

# Entry frame
frame = tk.Frame(root)
frame.pack(pady=10, padx=10)

tk.Label(frame, text="Tên sách:").grid(row=0, column=0, sticky='e', padx=5, pady=2)
entry_title = tk.Entry(frame, width=40)
entry_title.grid(row=0, column=1, columnspan=2, pady=2)

tk.Label(frame, text="Tác giả:").grid(row=1, column=0, sticky='e', padx=5, pady=2)
entry_author = tk.Entry(frame, width=40)
entry_author.grid(row=1, column=1, columnspan=2, pady=2)

tk.Label(frame, text="Năm XB:").grid(row=2, column=0, sticky='e', padx=5, pady=2)
entry_year = tk.Entry(frame, width=40)
entry_year.grid(row=2, column=1, columnspan=2, pady=2)

tk.Label(frame, text="Thể loại:").grid(row=3, column=0, sticky='e', padx=5, pady=2)
entry_genre = tk.Entry(frame, width=40)
entry_genre.grid(row=3, column=1, columnspan=2, pady=2)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Thêm", command=add_book, width=10).pack(side=tk.LEFT, padx=2)
tk.Button(button_frame, text="Cập nhật", command=update_book, width=10).pack(side=tk.LEFT, padx=2)
tk.Button(button_frame, text="Xóa", command=delete_book, width=10).pack(side=tk.LEFT, padx=2)
tk.Button(button_frame, text="Làm mới", command=reload_books, width=10).pack(side=tk.LEFT, padx=2)

# Treeview
tree = ttk.Treeview(root, columns=("ID", "Tên sách", "Tác giả", "Năm XB", "Thể loại"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Tên sách", text="Tên sách")
tree.heading("Tác giả", text="Tác giả")
tree.heading("Năm XB", text="Năm XB")
tree.heading("Thể loại", text="Thể loại")

tree.column("ID", width=50)
tree.column("Tên sách", width=200)
tree.column("Tác giả", width=150)
tree.column("Năm XB", width=100)
tree.column("Thể loại", width=100)

tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
tree.bind('<<TreeviewSelect>>', on_tree_select)

# Add scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.configure(yscrollcommand=scrollbar.set)

# Initialize database
try:
    connection = connect_db('books')
    if connection:
        create_table(connection)
        connection.close()
except Exception as e:
    messagebox.showerror("Lỗi Database", f"Không thể kết nối database: {str(e)}")
    root.quit()

reload_books()
root.mainloop()