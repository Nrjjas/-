import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, action='encrypt'):
    result = ""
    for char in text:
        if char.isupper():
            offset = 65
        elif char.islower():
            offset = 97
        else:
            result += char
            continue

        if action == 'encrypt':
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += chr((ord(char) - offset - shift) % 26 + offset)
    return result

def process():
    text = entry_text.get("1.0", tk.END).strip()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Error", "Shift must be a number.")
        return

    action = var_action.get()
    result = caesar_cipher(text, shift, action)
    result_label.config(state='normal')
    result_label.delete("1.0", tk.END)
    result_label.insert(tk.END, result)
    result_label.config(state='disabled')

def copy_result():
    root.clipboard_clear()
    root.clipboard_append(result_label.get("1.0", tk.END).strip())
    messagebox.showinfo("Copied", "Result copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("Caesar Cipher")

tk.Label(root, text="Text:").pack()
entry_text = tk.Text(root, height=5, width=40)
entry_text.pack()

tk.Label(root, text="Shift:").pack()
entry_shift = tk.Entry(root)
entry_shift.insert(0, "3")
entry_shift.pack()

var_action = tk.StringVar(value="encrypt")
tk.Radiobutton(root, text="Encrypt", variable=var_action, value="encrypt").pack()
tk.Radiobutton(root, text="Decrypt", variable=var_action, value="decrypt").pack()

tk.Button(root, text="Run", command=process).pack(pady=5)

tk.Label(root, text="Result:").pack()
result_label = tk.Text(root, height=5, width=40, state='disabled')
result_label.pack()

tk.Button(root, text="Copy Result", command=copy_result).pack(pady=5)

root.mainloop()
