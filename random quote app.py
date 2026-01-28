import tkinter as tk
import random

# 📚 List of Quotes (Quote, Author)
quotes = [
    ("The best way to get started is to quit talking and begin doing.", "Walt Disney"),
    ("Don’t let yesterday take up too much of today.", "Will Rogers"),
    ("It’s not whether you get knocked down, it’s whether you get up.", "Vince Lombardi"),
    ("If you are working on something exciting, it will keep you motivated.", "Steve Jobs"),
    ("Success is not in what you have, but who you are.", "Bo Bennett"),
    ("Dream big and dare to fail.", "Norman Vaughan"),
    ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
]

# 🎲 Function to Show Random Quote
def new_quote():
    quote, author = random.choice(quotes)
    quote_label.config(text=f'"{quote}"')
    author_label.config(text=f"- {author}")

# 🖼 GUI Setup
root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("500x300")
root.config(bg="white")

# Quote Text
quote_label = tk.Label(root, text="", font=("Arial", 14), wraplength=450, bg="white", justify="center")
quote_label.pack(pady=30)

# Author Text
author_label = tk.Label(root, text="", font=("Arial", 12, "italic"), bg="white")
author_label.pack(pady=10)

# Button
tk.Button(root, text="New Quote", font=("Arial", 12), command=new_quote).pack(pady=20)

# Show quote when app starts
new_quote()

root.mainloop()
