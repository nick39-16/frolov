import tkinter as tk
from tkinter import ttk, messagebox
import json
import random

QUOTES_FILE = 'quotes.json'

def load_quotes():
    try:
        with open(QUOTES_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'quotes': [], 'history': []}

def save_quotes(data):
    with open(QUOTES_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def generate_quote():
    quotes = quote_data['quotes']
    filtered_quotes = quotes.copy()
    
    author_filter = entry_author.get()
    theme_filter = entry_theme.get()
    
    if author_filter:
        filtered_quotes = [q for q in filtered_quotes if q['author'].lower() == author_filter.lower()]
    if theme_filter:
        filtered_quotes = [q for q in filtered_quotes if q['theme'].lower() == theme_filter.lower()]
    
    if not filtered_quotes:
        messagebox.showinfo("Внимание", "Нет цитат по данному фильтру!")
        return
    
    selected_quote = random.choice(filtered_quotes)
    label_random_quote.config(text=f"{selected_quote['text']} ({selected_quote['author']})")
    quote_data['history'].append(selected_quote)
    save_quotes(quote_data)
    refresh_history()

def refresh_history():
    history_list.delete(0, tk.END)
    for idx, quote in enumerate(quote_data['history'][::-1]):
        history_list.insert(idx, f"{quote['text']} ({quote['author']})")

# Начальное состояние
quote_data = load_quotes()

# Интерфейс приложения
root = tk.Tk()
root.title("Random Quote Generator")

frame_input = ttk.Frame(root)
frame_input.pack(padx=10, pady=10)

ttk.Label(frame_input, text="Автор:").grid(row=0, column=0, sticky="W")
entry_author = ttk.Entry(frame_input)
entry_author.grid(row=0, column=1, pady=5)

ttk.Label(frame_input, text="Тема:").grid(row=1, column=0, sticky="W")
entry_theme = ttk.Entry(frame_input)
entry_theme.grid(row=1, column=1, pady=5)

btn_generate = ttk.Button(frame_input, text="Сгенерировать цитату", command=generate_quote)
btn_generate.grid(row=2, column=0, columnspan=2, pady=10)

label_random_quote = ttk.Label(frame_input, text="", font=("Arial", 14))
label_random_quote.grid(row=3, column=0, columnspan=2, pady=10)

# История цитат
frame_history = ttk.Frame(root)
frame_history.pack(padx=10, pady=10)

ttk.Label(frame_history, text="История цитат:", font=("Arial", 12)).pack()
history_list = tk.Listbox(frame_history, height=10, width=50)
history_list.pack()

refresh_history()

root.mainloop()
