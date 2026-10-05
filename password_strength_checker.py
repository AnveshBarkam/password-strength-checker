import tkinter as tk
from tkinter import messagebox
import re


def check_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning("Warning", "Please enter a password.")
        return

    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    result_label.config(text=f"Password Strength: {strength}")

    if suggestions:
        suggestion_label.config(
            text="Suggestions:\n" + "\n".join("• " + s for s in suggestions)
        )
    else:
        suggestion_label.config(
            text="Excellent! Your password meets all the basic checks."
        )


def clear_password():
    password_entry.delete(0, tk.END)
    result_label.config(text="Password Strength:")
    suggestion_label.config(text="")


root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x400")

title = tk.Label(
    root,
    text="Password Strength Checker",
    font=("Arial", 20, "bold")
)
title.pack(pady=25)

password_entry = tk.Entry(
    root,
    width=35,
    show="*",
    font=("Arial", 14)
)
password_entry.pack(pady=10)

check_button = tk.Button(
    root,
    text="Check Password",
    command=check_password,
    font=("Arial", 12)
)
check_button.pack(pady=10)

clear_button = tk.Button(
    root,
    text="Clear",
    command=clear_password,
    font=("Arial", 12)
)
clear_button.pack(pady=5)

result_label = tk.Label(
    root,
    text="Password Strength:",
    font=("Arial", 16, "bold")
)
result_label.pack(pady=20)

suggestion_label = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    justify="left"
)
suggestion_label.pack(pady=10)

root.mainloop()
