#2274802010592 - Bùi Thiện Nhân
import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Hàm tính tuổi
def calculate_age():
    try:
        birth_year = int(entry_year.get())
        current_year = datetime.now().year
        age = current_year - birth_year
        result_label.config(text=f"Tuổi của bạn là: {age}")
    except ValueError:
        result_label.config(text="Vui lòng nhập năm sinh hợp lệ!")

# Hàm xóa dữ liệu tuổi
def reset_age():
    entry_year.delete(0, tk.END)
    result_label.config(text="")

# Hàm tính toán phép cộng
def add():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result_add.config(text=f"Kết quả cộng: {num1 + num2}")
    except ValueError:
        result_add.config(text="Vui lòng nhập số hợp lệ!")

# Hàm xóa dữ liệu phép cộng
def reset_add():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_add.config(text="")

# Hàm tính toán phép trừ
def subtract():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result_subtract.config(text=f"Kết quả trừ: {num1 - num2}")
    except ValueError:
        result_subtract.config(text="Vui lòng nhập số hợp lệ!")

# Hàm xóa dữ liệu phép trừ
def reset_subtract():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_subtract.config(text="")

# Hàm tính toán phép nhân
def multiply():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result_multiply.config(text=f"Kết quả nhân: {num1 * num2}")
    except ValueError:
        result_multiply.config(text="Vui lòng nhập số hợp lệ!")

# Hàm xóa dữ liệu phép nhân
def reset_multiply():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_multiply.config(text="")

# Hàm tính toán phép chia
def divide():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 != 0:
            result_divide.config(text=f"Kết quả chia: {num1 / num2}")
        else:
            result_divide.config(text="Không thể chia cho 0")
    except ValueError:
        result_divide.config(text="Vui lòng nhập số hợp lệ!")

# Hàm xóa dữ liệu phép chia
def reset_divide():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_divide.config(text="")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Python GUI")

# Tạo Notebook để chứa các tab
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Tạo Tab 1 - Tính tuổi
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Tính tuổi")

# Thêm các phần tử vào tab 1
label_year = ttk.Label(tab1, text="Nhập năm sinh:")
label_year.grid(row=0, column=0, padx=10, pady=10)
entry_year = ttk.Entry(tab1)
entry_year.grid(row=0, column=1, padx=10, pady=10)

btn_calculate_age = ttk.Button(tab1, text="Tính tuổi", command=calculate_age)
btn_calculate_age.grid(row=1, column=0, padx=10, pady=10)

btn_reset_age = ttk.Button(tab1, text="Nhập lại", command=reset_age)
btn_reset_age.grid(row=1, column=1, padx=10, pady=10)

result_label = ttk.Label(tab1, text="")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Tạo Tab 2 - Tính toán
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Tính toán")

# Thêm các phần tử vào tab 2
label_num1 = ttk.Label(tab2, text="Số thứ nhất:")
label_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num1 = ttk.Entry(tab2)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = ttk.Label(tab2, text="Số thứ hai:")
label_num2.grid(row=1, column=0, padx=10, pady=10)
entry_num2 = ttk.Entry(tab2)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Phép cộng
btn_add = ttk.Button(tab2, text="Cộng", command=add)
btn_add.grid(row=2, column=0, padx=10, pady=10)
result_add = ttk.Label(tab2, text="")
result_add.grid(row=2, column=1, padx=10, pady=10)
btn_reset_add = ttk.Button(tab2, text="Nhập lại", command=reset_add)
btn_reset_add.grid(row=2, column=2, padx=10, pady=10)

# Phép trừ
btn_subtract = ttk.Button(tab2, text="Trừ", command=subtract)
btn_subtract.grid(row=3, column=0, padx=10, pady=10)
result_subtract = ttk.Label(tab2, text="")
result_subtract.grid(row=3, column=1, padx=10, pady=10)
btn_reset_subtract = ttk.Button(tab2, text="Nhập lại", command=reset_subtract)
btn_reset_subtract.grid(row=3, column=2, padx=10, pady=10)

# Phép nhân
btn_multiply = ttk.Button(tab2, text="Nhân", command=multiply)
btn_multiply.grid(row=4, column=0, padx=10, pady=10)
result_multiply = ttk.Label(tab2, text="")
result_multiply.grid(row=4, column=1, padx=10, pady=10)
btn_reset_multiply = ttk.Button(tab2, text="Nhập lại", command=reset_multiply)
btn_reset_multiply.grid(row=4, column=2, padx=10, pady=10)

# Phép chia
btn_divide = ttk.Button(tab2, text="Chia", command=divide)
btn_divide.grid(row=5, column=0, padx=10, pady=10)
result_divide = ttk.Label(tab2, text="")
result_divide.grid(row=5, column=1, padx=10, pady=10)
btn_reset_divide = ttk.Button(tab2, text="Nhập lại", command=reset_divide)
btn_reset_divide.grid(row=5, column=2, padx=10, pady=10)

#
root.mainloop()
