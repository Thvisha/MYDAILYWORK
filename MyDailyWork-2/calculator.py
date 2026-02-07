import tkinter as tk

# ---------------- Window ----------------
root = tk.Tk()
root.title("Colorful Mobile Calculator")
root.geometry("360x540")
root.configure(bg="#0f172a")
root.resizable(False, False)

# ---------------- Variables ----------------
expression = tk.StringVar()
history = tk.StringVar()

# ---------------- Display ----------------
display_frame = tk.Frame(root, bg="#020617", height=140)
display_frame.pack(fill="x")

history_label = tk.Label(
    display_frame,
    textvariable=history,
    bg="#020617",
    fg="#94a3b8",
    font=("Poppins", 14),
    anchor="e",
    padx=10
)
history_label.pack(fill="x", pady=(25, 0))

display = tk.Entry(
    display_frame,
    textvariable=expression,
    bg="#020617",
    fg="#22d3ee",
    font=("Poppins", 34, "bold"),
    bd=0,
    justify="right"
)
display.pack(fill="x", padx=10, pady=10)

# ---------------- Functions ----------------
def press(value):
    expression.set(expression.get() + str(value))

def clear():
    expression.set("")
    history.set("")

def calculate():
    try:
        history.set(expression.get())
        result = eval(expression.get())
        expression.set(str(result))
    except:
        expression.set("Error")

# ---------------- Buttons ----------------
btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(expand=True, fill="both", padx=10, pady=10)

def make_btn(text, row, col, bg, fg="white", cmd=None, colspan=1, rowspan=1):
    tk.Button(
        btn_frame,
        text=text,
        bg=bg,
        fg=fg,
        font=("Poppins", 16, "bold"),
        bd=0,
        activebackground="#1e293b",
        activeforeground="white",
        command=cmd,
        relief="flat",
        width=5,
        height=2
    ).grid(
        row=row,
        column=col,
        columnspan=colspan,
        rowspan=rowspan,
        padx=6,
        pady=6,
        sticky="nsew"
    )

# Row 0
make_btn("C", 0, 0, "#fb7185", cmd=clear)
make_btn("÷", 0, 1, "#f59e0b", cmd=lambda: press("/"))
make_btn("×", 0, 2, "#f59e0b", cmd=lambda: press("*"))
make_btn("−", 0, 3, "#f59e0b", cmd=lambda: press("-"))

# Row 1
make_btn("7", 1, 0, "#334155", cmd=lambda: press(7))
make_btn("8", 1, 1, "#334155", cmd=lambda: press(8))
make_btn("9", 1, 2, "#334155", cmd=lambda: press(9))
make_btn("+", 1, 3, "#f59e0b", cmd=lambda: press("+"))

# Row 2
make_btn("4", 2, 0, "#334155", cmd=lambda: press(4))
make_btn("5", 2, 1, "#334155", cmd=lambda: press(5))
make_btn("6", 2, 2, "#334155", cmd=lambda: press(6))
make_btn("=", 2, 3, "#22c55e", cmd=calculate, rowspan=2)

# Row 3
make_btn("1", 3, 0, "#334155", cmd=lambda: press(1))
make_btn("2", 3, 1, "#334155", cmd=lambda: press(2))
make_btn("3", 3, 2, "#334155", cmd=lambda: press(3))

# Row 4
make_btn("0", 4, 0, "#334155", cmd=lambda: press(0), colspan=2)
make_btn(".", 4, 2, "#334155", cmd=lambda: press("."))

# Grid resize
for i in range(5):
    btn_frame.rowconfigure(i, weight=1)
for j in range(4):
    btn_frame.columnconfigure(j, weight=1)

root.mainloop()