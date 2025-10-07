import tkinter as tk
from PIL import Image, ImageTk
import qrcode

# ---------- Functions ----------
def generate():
    upi = entry.get().strip()
    if upi and upi != placeholder_text:
        img = qrcode.make(f"upi://pay?pa={upi}&pn=Recipient").resize((300, 300))
        global qr_img
        qr_img = ImageTk.PhotoImage(img)
        label_qr.config(image=qr_img)

def on_entry_click(event):
    if entry.get() == placeholder_text:
        entry.delete(0, "end")
        entry.config(fg="black")

def on_focusout(event):
    if entry.get() == "":
        entry.insert(0, placeholder_text)
        entry.config(fg="grey")

# ---------- GUI ----------
root = tk.Tk()
root.title("UPI QR Code Generator")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

# Set window size and center it
window_width = 400
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# Heading
heading = tk.Label(root, text="UPI QR Generator", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
heading.pack(pady=20)

# Entry with placeholder
placeholder_text = "Enter UPI ID here"
entry = tk.Entry(root, font=("Arial", 14), width=25, justify='center', fg="grey")
entry.insert(0, placeholder_text)
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_focusout)
entry.pack(pady=10)

# Generate button
btn = tk.Button(root, text="Generate QR", font=("Arial", 14), bg="#4CAF50", fg="white", command=generate)
btn.pack(pady=20)

# QR Code display
label_qr = tk.Label(root, bg="#f0f0f0")
label_qr.pack(pady=20)

root.mainloop()
