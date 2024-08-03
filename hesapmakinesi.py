import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
# Hesap makinesi işlevlerini tanımlayın
def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        if expression == "2+2":
            result = "Deniz"
            messagebox.showinfo("Uyarı", "Deniz yazıldı!")
            show_image()
        elif expression == "5+3":
            result = "Recep"
        else:
            result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Hata")

def show_image():
    top = tk.Toplevel()
    top.title("Deniz Resmi")
    image = Image.open("deniz_resmi.jpg")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(top, image=photo)
    label.image = photo
    label.pack()

# Tkinter penceresini oluşturun
window = tk.Tk()
window.title("Hesap Makinesi")

# Giriş alanı
entry = tk.Entry(window, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
entry.grid(row=0, column=0, columnspan=4)

# Butonları oluşturun
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':
        tk.Button(window, text=button, width=5, height=2, command=clear, bg='red', fg='white', font=('Arial', 16, 'bold')).grid(row=row_val, column=col_val)
    elif button == '=':
        tk.Button(window, text=button, width=5, height=2, command=calculate, bg='green', fg='white', font=('Arial', 16, 'bold')).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, width=5, height=2, command=lambda b=button: click_button(b), bg='lightblue', fg='black', font=('Arial', 16, 'bold')).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Pencereyi başlat
window.mainloop()
