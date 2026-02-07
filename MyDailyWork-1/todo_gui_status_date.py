import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# ---------------- Window ----------------
root = tk.Tk()
root.title("Daily Planner ✨")
root.geometry("650x600")
root.configure(bg="#eef2ff")

tasks = []

# ---------------- Header ----------------
header = tk.Frame(root, bg="#cd27ba", height=90)
header.pack(fill="x")

title = tk.Label(
    header,
    text="Daily Planner",
    font=("Arial", 22, "bold"),
    bg="#cd27ba",
    fg="white"
)
title.place(x=20, y=25)

subtitle = tk.Label(
    header,
    text="Organize • Focus • Achieve",
    font=("Segoe UI", 11),
    bg="#cd27ba",
    fg="#dcdde1"
)
subtitle.place(x=22, y=60)

# ---------------- Card ----------------
card = tk.Frame(root, bg="white", bd=0)
card.pack(pady=10, padx=20, fill="both", expand=True)

# ---------------- Inputs ----------------
input_frame = tk.Frame(card, bg="white")
input_frame.pack(pady=15)

task_label = tk.Label(
    input_frame,
    text="Task",
    bg="white",
    fg="#2f3640",
    font=("Segoe UI", 10, "bold")
)
task_label.grid(row=0, column=0, sticky="w", padx=5)

task_entry = tk.Entry(
    input_frame,
    width=28,
    font=("Segoe UI", 12),
    bd=2,
    relief="groove"
)
task_entry.grid(row=1, column=0, padx=5, pady=3)

date_label = tk.Label(
    input_frame,
    text="Due Date (YYYY-MM-DD)",
    bg="white",
    fg="#2f3640",
    font=("Segoe UI", 10, "bold")
)
date_label.grid(row=0, column=1, sticky="w", padx=5)

date_entry = tk.Entry(
    input_frame,
    width=15,
    font=("Segoe UI", 12),
    bd=2,
    relief="groove"
)
date_entry.grid(row=1, column=1, padx=5, pady=3)
time_label = tk.Label(
    input_frame,
    text="Time (HH:MM - HH:MM)",
    bg="white",
    fg="#2f3640",
    font=("Arial", 10, "bold")
)
time_label.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=(8, 0))

time_entry = tk.Entry(
    input_frame,
    width=25,
    font=("Arial", 12),
    bd=2,
    relief="groove"
)
time_entry.grid(row=3, column=0, columnspan=2, padx=5, pady=3)

# ---------------- Listbox ----------------
task_listbox = tk.Listbox(
    card,
    width=70,
    height=10,
    font=("Segoe UI", 11),
    bg="#f8f9ff",
    fg="#2f3640",
    selectbackground="#c7d2fe",
    bd=0,
    highlightthickness=0
)
task_listbox.pack(pady=10, padx=15)

# ---------------- Functions ----------------
def refresh():
    task_listbox.delete(0, tk.END)
    today = datetime.today().date()

    for t in tasks:
        due = datetime.strptime(t["date"], "%Y-%m-%d").date()

        if t["status"] == "Completed":
            text = f"✔ {t['task']} | {t['date']} | {t['time']}"

        elif due < today:
            text = f"⏰ {t['task']} | {t['date']} | {t['time']} (Overdue)"

        else:
            text = f"⏳ {t['task']} | {t['date']} | {t['time']}"

        task_listbox.insert(tk.END, text)

def add_task():
    task = task_entry.get()
    date = date_entry.get()
    time = time_entry.get()

    # Validate date
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except:
        messagebox.showwarning("Date Error", "Use YYYY-MM-DD")
        return

    # Validate time
    if "-" not in time:
        messagebox.showwarning("Time Error", "Use HH:MM - HH:MM")
        return

    if task.strip() == "":
        messagebox.showwarning("Task Missing", "Enter a task")
        return

    tasks.append({
        "task": task,
        "date": date,
        "time": time,
        "status": "Pending"
    })

    refresh()
    task_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)

def complete_task():
    try:
        i = task_listbox.curselection()[0]
        tasks[i]["status"] = "Completed"
        refresh()
    except:
        messagebox.showinfo("Select Task", "Select a task first")

def delete_task():
    try:
        i = task_listbox.curselection()[0]
        tasks.pop(i)
        refresh()
    except:
        messagebox.showinfo("Select Task", "Select a task to delete")

# ---------------- Buttons ----------------
btn_frame = tk.Frame(card, bg="white")
btn_frame.pack(pady=15)

def styled_btn(text, color, cmd):
    return tk.Button(
        btn_frame,
        text=text,
        width=14,
        font=("Segoe UI", 10, "bold"),
        bg=color,
        fg="white",
        bd=0,
        activebackground="#2d3436",
        cursor="hand2",
        command=cmd
    )

styled_btn("➕ Add Task", "#6c5ce7", add_task).grid(row=0, column=0, padx=6)
styled_btn("✔ Complete", "#00b894", complete_task).grid(row=0, column=1, padx=6)
styled_btn("🗑 Delete", "#d63031", delete_task).grid(row=0, column=2, padx=6)

# ---------------- Footer ----------------
footer = tk.Label(
    root,
    text="Made with ❤️ using Python & Tkinter",
    bg="#eef2ff",
    fg="#636e72",
    font=("Segoe UI", 9)
)
footer.pack(pady=8)

root.mainloop()